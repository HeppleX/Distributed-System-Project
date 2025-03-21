from app.models import Student,session

def authenticate_student(student_id, password):
    student = session.query(Student).filter(
        Student.student_id == student_id,
        Student.password_hash == password
    ).first()
    return student
