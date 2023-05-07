from fastapi import APIRouter
from utils.TestData import get_all_faculty, get_cafedra_by_faculty

router = APIRouter()

@router.get("/getFilterFacultyTeacher")
def get_filter_teacher():
        return get_all_faculty()

@router.get("/getFiltersCafedraWeek")
def get_filter_teacher(faculty: str):
        return [{'cafedra':get_cafedra_by_faculty(faculty),
                 'week': [number_week for number_week in range(1,10)]}]


@router.get("/getTeacherByFilter")
def get_teacher_by_filter(faculty: str, cafedra: str):
        get

# @router.get("/groupByFilter")
# def group_by_filter(faculty: str, course: int):
#     return get_group_by_filter(faculty=faculty, course=course)