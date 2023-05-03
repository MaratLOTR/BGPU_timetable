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

def get_list_enable_value_group():
    return {
    "faculty": [
                "ФИРТ",
                "ИНЭК"
                ],
    "course": [
                "1",
                "2",
                "3",
                "4",
              ],
    "group": [
                "ПРО-323",
                "ПРО-329",
                "ПРО-222",
                "ПРО-414"
            ],
    "week": [
                "1",
                "2",
                "3",
                "4"
            ]
}

def get_list_enable_value_group():
    return {
            "numberOfWeek": [
                "1",
                "2",
                "3",
                "4"
                ],
            "corpus": [
            "1",
            "2",
            "3",
            "4",
            ],
            "auditory": [
            "9-231",
            "1-111",
            "2-222",
            "6-666"
            ]
            }

# {'week': [1, 2, 3, 4],
#   {'faculty': 'FIRT',
#    'data': [{
#        'course':1
#    }]
#    'group': ['ПРО-329', 'МО-422']},
#  {'faculty': 'INEK',
#   'group': ['I-1111', 'M-123']}
# }