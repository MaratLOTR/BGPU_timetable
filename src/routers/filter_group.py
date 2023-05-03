from fastapi import APIRouter
from datetime import datetime
from dataclasses import dataclass
router = APIRouter()
from db_pack import fake_query
group_by_filter = [{
		"faculty": "ФИРТ",
		"data": [
		{
			"course": 1,
			"group": ["МО-111", "ПРО-123"]
		},
		{
			"course": 2,
			"group": ["МО-222", "ПРО-223"]
		},
		{
			"course": 3,
			"group": ["МО-333", "ПРО-329"]
		}
				]
	},
	{
		"faculty": "ИНЭК",
		"data": [
		{
			"course": 1,
			"group": ["И-111", "М-123"]
		},
		{
			"course": 2,
			"group": ["И-222", "М-223"]
		},
		{
			"course": 3,
			"group": ["И-333", "М-367"]
		}
				]
	}]

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

@router.get("/group_by_filter")
def get_group_by_filter(faculty: str, course: int):
    for filt in group_by_filter:
        if filt['faculty'] == faculty:
            for cour in filt['data']:
                if cour['course'] == course:
                    return cour['group']