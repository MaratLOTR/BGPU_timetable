from .data_for_schedule import TypeOfTheLesson


def get_group_schedule(faculty, course, week, group):
    return [{
                "lessonName": "Компьютерная графика",
                "classRoom": "6-322",
                "lessonTypeColor": "1",
                "lessonType": TypeOfTheLesson.exam.value,
                "teacherName": "Иванов И.И.",
                "startSubject": "8:00",
                "endSubject": "9:35"
            },
            {
                "lessonName": "Компьютерная инженерия",
                "classRoom": "6-412",
                "lessonTypeColor": "2",
                "lessonType": TypeOfTheLesson.lecture,
                "teacherName": "Сидоров Н.К.",
                "startSubject": "9:45",
                "endSubject": "11:20"
            },
            {
                "lessonName": "Компьютерная графика",
                "classRoom": "6-122",
                "lessonTypeColor": "3",
                "lessonType": TypeOfTheLesson.practice,
                "teacherName": "Куполов С.А.",
                "startSubject": "12:10",
                "endSubject": "13:45"
            }]