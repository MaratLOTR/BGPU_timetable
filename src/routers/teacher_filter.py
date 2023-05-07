from fastapi import APIRouter
from utils.TestData import get_all_faculty, get_cafedra_by_faculty

router = APIRouter()

@router.get("/getFaculty")
def get_filter_teacher():
        return get_all_faculty()

@router.get("/getCafedraByFaculty")
def get_filter_teacher(faculty: str):
        return get_cafedra_by_faculty(faculty)




# @router.get("/groupByFilter")
# def group_by_filter(faculty: str, course: int):
#     return get_group_by_filter(faculty=faculty, course=course)