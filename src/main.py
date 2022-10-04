from parser_excel.excel import Parser
import os
from db.database import Base, engine, SessionLocal
from db.crud import insert_database


if __name__ == '__main__':
    excel_path = []
    Base.metadata.create_all(engine)
    for address, dirs, files in os.walk('C:/Домашняя работа/Управление проектами/schedule_excel'):
        for name in files:
            excel_path.append(os.path.join(address, name))
    for path in excel_path:
        path = path.replace('~$','')
        parser = Parser(path)
        data = parser.parse()
        insert_database(session=SessionLocal(),data=data)
