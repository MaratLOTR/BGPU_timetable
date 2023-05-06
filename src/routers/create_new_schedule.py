import random
import datetime
from utils.date import get_day_of_the_week_by_date
from utils.TestData import list_of_lesson_name, list_of_time_lesson, list_of_type_lesson, list_of_teacher_name
class PairTeacherLesson:
    def __init__(self, teacher, lesson):
        self.teacher = teacher
        self.lesson = lesson


def generate_pair_teacher_lesson():
    list_of_pair_lesson_teacher = []
    for teacher in list_of_teacher_name:
        k = random.randint(1,2)
        for i in range(k):

            if len(list_of_lesson_name) != 0:
                lesson = list_of_lesson_name[random.randint(0, len(list_of_lesson_name) - 1)]
                list_of_pair_lesson_teacher.append(PairTeacherLesson(teacher, lesson))
                list_of_lesson_name.remove(lesson)
    return list_of_pair_lesson_teacher


def generate_schedule_in_day(list_of_pair_lesson_teacher, group:str, number_lesson: int, number_of_week: int, day: int):
    k = random.randint(0, len(list_of_pair_lesson_teacher)-1)
    date = datetime.datetime.strptime('2022-09-05', "%Y-%m-%d")
    date = date+datetime.timedelta(weeks=number_of_week, days=day)
    schedule_in_a_day = {
        'lessonName':list_of_pair_lesson_teacher[k].lesson,
        'teacherName':list_of_pair_lesson_teacher[k].teacher,
        'classRoom': str(random.randint(1,9))+"-"+str(random.randint(1,9)*100+random.randint(1,9)*10+random.randint(1,9)),
        'lessonType': list_of_type_lesson[random.randint(0,1)],
        'startSubject': list_of_time_lesson[number_lesson][0],
        'endSubject': list_of_time_lesson[number_lesson][1],
        'date': str(date.day),
        'dayOfTheWeek':get_day_of_the_week_by_date(date),
        'week': str(number_of_week),
        'groupName': group
    }
    return schedule_in_a_day


def create_fake_schedule():
    data = []
    list_of_group = ["МО-111", "ПРО-123", "МО-211", "ПРО-229", "МО-333", "ПРО-329", "И-111", "М-123", "И-222", "М-223",
                     "И-333", "М-323", "МО-444", "ПРО-429","И-444", "М-423"]
    list_of_pair_teacher_lesson = generate_pair_teacher_lesson()
    for group in list_of_group:
        for week in range(0,10):
            for day in range(0,6):
                count_of_lesson = random.randint(1,4)
                for number_of_lesson in range(1, count_of_lesson):
                    schedule_data = generate_schedule_in_day(list_of_pair_teacher_lesson,group, number_of_lesson, week, day)
                    data.append(schedule_data)
    return data

if __name__ == '__main__':
    with open('test_data.txt','w') as file:
        for d in create_fake_schedule():
            file.write(str(d)+'\n')