from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models import Student, Course, Enrollment, session
from app.utils import authenticate_student
from datetime import datetime

# User Login
class LoginAPI(Resource):
    def post(self):
        # print("test")
        data = request.get_json()
        student_id = data.get("student_id")
        password = data.get("password")

        student = authenticate_student(student_id, password)
        if not student:
            return {"message": "Invalid student ID or password"}, 401

        # Check if the student exists
        student_record = session.query(Student).filter_by(student_id=student_id).first()
        if not student_record:
            return {"message": "Student not found"}, 404

        access_token = create_access_token(identity=student_id)
        return {
            "access_token": access_token,
            "student_name": student_record.student_name
        }, 200
    
# Search Class Information API
class CourseListAPI(Resource):
    def get(self):
        courses = session.query(Course).all()
        course_list = [
            {
                "course_id": course.course_id,
                "course_name": course.course_name,
                "start_time": str(course.start_time),
                "end_time": str(course.end_time),
                "current_enrollment": course.current_enrollment,
                "total_seats": course.total_seats,
            }
            for course in courses
        ]
        return jsonify({"courses": course_list})
    
# Select Course API
class EnrollAPI(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        data = request.get_json()
        course_id = data.get("course_id")

        course = session.query(Course).filter_by(course_id=course_id).first()
        if not course or course.total_seats <= course.current_enrollment:
            return {"message": "Course not available or full"}, 400

        # Check if the course is already selected
        existing_enrollment = session.query(Enrollment).filter_by(student_id=current_user, course_id=course_id).first()
        if existing_enrollment:
            return {"message": "You have already enrolled in this course"}, 400

        student = session.query(Student).filter(Student.student_id == current_user).first()

        # Create a new enrollment record
        new_enrollment = Enrollment(student_id=current_user,student_name=student.student_name,
                                    course_id=course_id,course_name=course.course_name,
                                    enroll_time=datetime.now())
        course.current_enrollment += 1
        session.add(new_enrollment)
        session.commit()

        return {"message": "Course enrolled successfully"}, 200

# Drop Course API
class DropAPI(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        data = request.get_json()
        course_id = data.get("course_id")

        enrollment = session.query(Enrollment).filter_by(student_id=current_user, course_id=course_id).first()
        if not enrollment:
            return {"message": "You are not enrolled in this course"}, 400

        # Check if the course is already selected
        course = session.query(Course).filter_by(course_id=course_id).first()
        session.delete(enrollment)
        course.current_enrollment -= 1
        session.commit()

        return {"message": "Course dropped successfully"}, 200

# Get Student Schedule API
class ScheduleAPI(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        enrollments = session.query(Enrollment).filter_by(student_id=current_user).all()
        schedule = []

        for enrollment in enrollments:
            course = session.query(Course).filter_by(course_id=enrollment.course_id).first()
            schedule.append({"course_id": course.course_id, "course_name": course.course_name, "enroll_time": enrollment.enroll_time})

        return jsonify(schedule)

# Initialize API routes
def initialize_routes(api):
    api.add_resource(LoginAPI, "/login")
    api.add_resource(EnrollAPI, "/enroll")
    api.add_resource(DropAPI, "/drop")
    api.add_resource(ScheduleAPI, "/schedule")
    api.add_resource(CourseListAPI, "/courses")
