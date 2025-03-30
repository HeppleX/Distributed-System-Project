from sqlalchemy import Column, BigInteger, String, Integer, Date,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
# Create MySQL Connection
DATABASE_URL = "mysql+pymysql://root:root@localhost/course_selection_db"
engine = create_engine(DATABASE_URL)

# Create Session
Session = sessionmaker(bind=engine)
session = Session()

class Course(Base):
    __tablename__ = 'course'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    course_id = Column(BigInteger, nullable=False, index=True)
    course_name = Column(String(255), nullable=False)
    start_time = Column(Date, nullable=False, comment='Course start time')
    end_time = Column(Date, nullable=False, comment='Course completion time')
    current_enrollment = Column(Integer, nullable=True, comment='Current enrollment')
    total_seats = Column(Integer, nullable=True, comment='Total capacity')


class Student(Base):
    __tablename__ = 'student'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    student_id = Column(BigInteger, nullable=False, index=True)
    student_name = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)


class Enrollment(Base):
    __tablename__ = 'enrollment'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    student_id = Column(BigInteger, nullable=False)
    student_name = Column(String(255), nullable=False)
    course_id = Column(BigInteger, nullable=False)
    course_name = Column(String(255), nullable=False)
    enroll_time = Column(DateTime(timezone=True),nullable=False)
