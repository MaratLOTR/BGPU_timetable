import json
import random
import datetime
list_of_lesson_name = ["Oneal",
                            "Duarte",
                            "Brown",
                            "Marsh",
                            "Silva",
                            "Petersen"]
list_of_teacher_name = ["Oneal",
                            "Duarte",
                            "Brown",
                            "Marsh",
                            "Silva",
                            "Petersen",
                            "Mcpherson",
                            "Ferguson",
                            "Hampton",
                            "Nash",
                            "Branch",
                            "Calderon"]
list_of_type_lesson = ['Lecture', 'Practice']
list_of_time_lesson = {1: ['8:00', '9:35'],
                       2: ['9:45', '11:20'],
                       3: ['12:10', '13:45'],
                       4: ['13:55', '15:30']}
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

def generate_schedule_in_day(list_of_pair_lesson_teacher, number_lesson, number_of_week, day):
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
        'dayOfTheWeek':get_day_of_the_week_by_date(date)
    }
    return schedule_in_a_day


def create_fake_schedule():
    data = []
    list_of_group = ["МО-111", "ПРО-123", "МО-211", "ПРО-223", "МО-333", "ПРО-329", "И-111", "М-123", "И-222", "М-223",
                     "И-333", "М-367"]
    list_of_pair_teacher_lesson = generate_pair_teacher_lesson()
    for group in list_of_group:
        for week in range(0,10):
            for day in range(0,6):
                count_of_lesson = random.randint(1,4)
                for number_of_lesson in range(1, count_of_lesson):
                    schedule_data = generate_schedule_in_day(list_of_pair_teacher_lesson, number_of_lesson, week, day)
                    schedule_data['week']=str(week)
                    schedule_data['groupName'] = group
                    data.append(schedule_data)
    return data

if __name__ == '__main__':
    with open('test_data.txt','w') as file:
        for d in create_fake_schedule():
            file.write(str(d)+'\n')