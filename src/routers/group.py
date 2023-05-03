from fastapi import APIRouter
from datetime import datetime
from dataclasses import dataclass
router = APIRouter()
from db_pack import fake_query



@router.get("/group/{group}")
def group_filter(faculty: str, course: str, group: str, week: int):
    return fake_query.get_group_schedule(faculty=faculty, course=course,week=week, group=group)

@router.get("/group")
def get_enable_filter_group():
    return fake_query.get_list_enable_value_group()

@router.get("/auditory")
def get_enable_filter_auditory():
    return