from pydantic import BaseModel

class Info(BaseModel):
    faculty: str
    group: str
    course: int
    class Config:
        orm_mode = True

class BaseGroup(BaseModel):
    faculty: str
    group: str
    course: int
    class Config:
        orm_mode = True

class GroupFilter(BaseGroup):
    week: int
    class Config:
        orm_mode = True

