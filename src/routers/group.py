from fastapi import APIRouter

router = APIRouter()
from utils.date import get_days_by_week


@router.get("/getDaysOfWeek")
def get_date_by_week(week: str):
    if week != "":
        print("week", week)
        return get_days_by_week(int(week))
    else:
        return get_days_by_week(4)
        #return [{'date': "date.day", "day_of_the_week": "day_of_week"}]


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
            del response_sch['cafedra']
            schedule_in_a_day.append(response_sch)
    return schedule_in_a_day
