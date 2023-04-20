from fastapi import Depends, FastAPI, HTTPException
from routers import group

#from db_pack.crud import Database
#from db import crud, model
import schemas
#from db.database import SessionLocal, engine


app = FastAPI()
#app.include_router(group.group_filter)
#
@app.get("/filter")
def filter(faculty: str, group: str, week:int):
    return {123}
    #db = Database()
    #res = db.get_list_group_and_student(faculty, name_group= group)
    #return res



