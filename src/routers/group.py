from fastapi import APIRouter
router = APIRouter()
from db_pack import fake_query
import datetime
from .create_new_schedule import create_fake_schedule
def get_day_of_the_week_by_date(date):
    day_of_the_week = {1:"Пн",
                       2:"Вт",
                       3:"Ср",
                       4:"Чт",
                       5:"Пт",
                       6:"Сб",
                       7:"Вс"}
    number_day_of_the_week = date.isoweekday()
    return day_of_the_week[number_day_of_the_week]

def get_days_by_week(number_of_week:int):
    date = datetime.datetime.strptime('2022-09-05', "%Y-%m-%d")
    date = date + datetime.timedelta(weeks=int(number_of_week))
    date_day_of_week = []

    for i in range(6):
        day_of_week = get_day_of_the_week_by_date(date)
        date_day_of_week.append({'date': date.day, "day_of_the_week": day_of_week})
        date = date + datetime.timedelta(days=1)
    return date_day_of_week


@router.get("/group/{group}")
def group_filter(faculty: str, course: str, group: str, week: int):
    return fake_query.get_group_schedule(faculty=faculty, course=course,week=week, group=group)

@router.get("/group")
def get_enable_filter_group():
    return fake_query.get_list_enable_value_group()

@router.get("/auditory")
def get_enable_filter_auditory():
    return
# @router.get("/schedule_123")

@router.get("/getDaysOfWeek")
def get_date_by_week(week:str):
    return [get_days_by_week(int(week))]


schedule = create_fake_schedule()
@router.get("/scheduleForADay")
def get_schedule_for_day(group: str, week: str, day_of_the_week: str):
    schedule_in_a_day = []
    for sch in schedule:
        if sch['groupName'] == group and sch['week'] == week and sch['dayOfTheWeek'] == day_of_the_week:
            response_sch = sch.copy()
            del response_sch['week']
            del response_sch['groupName']
            del response_sch['date']
            del response_sch['dayOfTheWeek']
            # response_sch.pop('week')
            # response_sch.pop('groupName')
            # response_sch.pop('date')
            # response_sch.pop('dayOfTheWeek')
            schedule_in_a_day.append(response_sch)
    return schedule_in_a_day