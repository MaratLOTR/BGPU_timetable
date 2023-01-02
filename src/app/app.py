from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from db.crud import Database
#from db import crud, model
import schemas
#from db.database import SessionLocal, engine


app = FastAPI()

@app.post("/filter")
def filter(faculty: str, group: str, week:int):
    db = Database()
    res = db.get_list_group_and_student(faculty, name_group= group)
    return res

