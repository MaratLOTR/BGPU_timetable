from .excel import Parser_Excel
import os
from db.database import Base, engine, SessionLocal
from db.crud import Database
import logging


def start_parser(Path: str):
    excel_path = []
    Base.metadata.create_all(engine)
    db = Database()
    for address, dirs, files in os.walk(Path):
        for name in files:
            excel_path.append(os.path.join(address, name))
    for path in excel_path:
        path = path.replace('~$', '')
        groups = db.get_list_group()
        auditorys = db.get_list_auditory()
        teachers = db.get_list_teacher()
        subjects = db.get_list_subject()
        parser = Parser_Excel(path, groups=groups, teachers=teachers, auditorys=auditorys,
                              subjects=subjects)
        parser.parse()

        db.insert_database(data=parser.output_data)
    db.get_list_group_and_student('','')
