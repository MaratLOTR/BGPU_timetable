from pydantic import BaseModel

class Info(BaseModel):
    faculty: str
    group: str
    course: int

    class Config:
        orm_mode = True
