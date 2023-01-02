from sqlalchemy import Integer, String, Column, Date, ForeignKey, DateTime
from db.database import Base
from sqlalchemy.orm import relationship


class Schedule(Base):
    __tablename__ = 'schedule'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_group = Column(String)
    faculty = Column(String)
    type = Column(String(10), nullable=False)
    name_subject = Column(String(200), nullable=False)
    name_teacher = Column(String(50), nullable=False)
    auditory = Column(String(200), nullable=False)
    time = Column(String)
    date = Column(DateTime)


class Faculty(Base):
    __tablename__ = 'faculty'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    id_faculty = Column(Integer, ForeignKey('faculty.id'))
    faculty = relationship('Faculty')


class Auditory(Base):
    __tablename__ = 'auditory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


class Subject(Base):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


class Group(Base):
    __tablename__ = 'uchgroup'
    id = Column(Integer, primary_key=True, autoincrement=True)
    course = Column(Integer)
    spec = Column(String)
    number = Column(Integer)
    id_faculty = Column(Integer, ForeignKey('faculty.id'))

    faculty = relationship('Faculty')


class Lesson(Base):
    __tablename__ = 'lesson'
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer)
    types = Column(Integer)
    date = Column(Date)
    id_subject = Column(Integer, ForeignKey('subject.id'))
    id_auditory = Column(Integer, ForeignKey('auditory.id'))
    subject = relationship('Subject')
    auditory = relationship('Auditory')


class TimeTable(Base):
    __tablename__ = 'timetable'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_group = Column(Integer, ForeignKey('uchgroup.id'))
    id_lesson = Column(Integer, ForeignKey('lesson.id'))
    id_teacher = Column(Integer, ForeignKey('teacher.id'))
    group = relationship('Group')
    lesson = relationship('Lesson')
    teacher = relationship('Teacher')