import datetime
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