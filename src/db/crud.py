from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL_CONFIG
from .model import *
from sqlalchemy import select
from datetime import datetime


class Database:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL_CONFIG)
        Session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.session = Session()
        self.Base = declarative_base()

    def insert_database(self, data: list):
        #obj = Schedule(*data)
        self.session.add_all(data)
        self.session.commit()


        # obj = Teacher(name='aaa', faculty=Faculty(name='fac1'))
        # self.session.add(obj)
        # self.session.commit()
        # print(self.get_list_teacher())

    def get_list_teacher(self):
        result = self.session.query(Teacher).all()
        return [res.name for res in result]

    def get_list_auditory(self):
        result = self.session.query(Auditory).all()
        return [res.name for res in result]

    def get_list_subject(self):
        result = self.session.query(Subject).all()
        return [res.name for res in result]

    def get_list_group(self):
        result = self.session.query(Group).all()
        return [res.name for res in result]

    def get_list_group_and_student(self, faculty, name_group):
        res = self.session.query(Schedule.faculty, Schedule.name_group).where(Schedule.faculty==faculty).\
            where(Schedule.name_group == name_group).distinct().all()
        print(res)
        return res
# obj = TimeTable()
# obj(group = )
# obj.group.faculty.name = 'FIRT'
# obj.group.spec='Pro'
# obj.group.course = 3
# obj.group.number = 29
# obj.teacher.name="Messi"
# obj.teacher.faculty.name = 'ASU'
# obj.lesson.date = datetime.now()
# obj.lesson.number = 3
# obj.lesson.types = 0
# obj.lesson.subject.name = 'DB'
# obj.lesson.auditory.name = '6-119'
