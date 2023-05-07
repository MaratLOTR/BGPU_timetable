from fastapi import APIRouter
from utils.TestData import get_group_by_filter

router = APIRouter()


@router.get("/getFilterFacultyCourseWeek")
def get_all_faculty():
    return [{"faculty": ["ФИРТ", "ИНЭК", ], "course": list(str(i) for i in range(1, 5)),
             "week": list(str(i) for i in range(1, 25))}
            ]


###КОНЕЦ СПОРНОГО КОДА
@router.get("/groupByFilter")
def group_by_filter(faculty: str, course: int):
    if faculty != "" and course != None:
        return get_group_by_filter(faculty=faculty, course=course)
