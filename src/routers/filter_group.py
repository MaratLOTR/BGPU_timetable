from fastapi import APIRouter
from utils.TestData import get_group_by_filter

router = APIRouter()


#!!!
#СЕМЕН, ПРОВЕРЬ ТАК ЛИ У ТЕБЯ ВЫГЛЯДИТ ЭТОТ УЧАСТОК КОДА
#ПРАВИЛЬНАЯ ВЕРСИЯ У ТЕБЯ, ПОЭТОМУ ОСТАВЛЯЙ СВОЙ ВАРИАНТ
#!!!
#Начало спорного кода
@router.get("/filter_faculty")
def get_all_faculty():
    return  [
                "ФИРТ",
                "ИНЭК",
                ]

@router.get("/filter_course")
def get_all_course():
    return list(i for i in range(1,5))

@router.get("/filter_week")
def get_all_week():
    return  list(i for i in range(1,25))

###КОНЕЦ СПОРНОГО КОДА
@router.get("/groupByFilter")
def group_by_filter(faculty: str, course: int):
    return get_group_by_filter(faculty=faculty, course=course)