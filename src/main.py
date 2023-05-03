from fastapi import Depends, FastAPI, HTTPException
from routers import group
import uvicorn
#from db_pack.crud import Database
#from db import crud, model
from routers import group, filter_group
#from db.database import SessionLocal, engine


app = FastAPI()
app.include_router(group.router)
app.include_router(filter_group.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
# #
# @app.get("/filter")
# def filter(faculty: str, group: str, week:int):
#     return {123}
#     db = Database()
#     res = db.get_list_group_and_student(faculty, name_group= group)
#     return res







# from parser_excel.main_parser import start_parser
#
#
# if __name__ == '__main__':
#     start_parser('C:/Домашняя работа/Управление проектами/schedule_excel')