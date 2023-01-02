import openpyxl
from datetime import datetime
import collections
from db.model import *
from abc import ABC, abstractmethod
import random


faculty = ['ФИРТ','АВИЭТ']


class BaseDataProcess(ABC):

    def __init__(self, name_group = None):
        self.__file = None
        self.name_group = name_group
        self.output_data = []

    @abstractmethod
    def parse(self):
        pass

class Parser_Excel(BaseDataProcess):
    def __init__(self, full_path: str, **kwargs):
        BaseDataProcess.__init__(self)
        self.__file = openpyxl.load_workbook(full_path)
        self.name_group = full_path[full_path.find('(')+1 : full_path.find(',')]
        self.sheet = self.__file.active
        # self.spec = name_group.split('-')[0]
        # self.course = name_group.split('-')[1][0]
        # self.number = name_group.split('-')[1][1:]
        # self.output_data = []
        # self.subjects = kwargs['subjects']
        # self.groups = kwargs['groups']
        # self.teachers = kwargs['teachers']
        # self.auditorys = kwargs['auditorys']
        self.faculty = faculty[random.randint(0, 1)]
        print()
    def parse(self):
        length = self.sheet.max_row
        old_timetable = {}
        schedule = []

        #timetable = TimeTable(faculty=Faculty(name='FIRT'))
        for i in range(2, length + 1):
            value = self.sheet.cell(row=i, column=1).value
            try:
                date = datetime.strptime(value, "%d.%m.%Y")
                old_timetable[date] = {}
                schedule.append(Schedule(date=date))
                schedule[-1].faculty = self.faculty
                schedule[-1].name_group = self.name_group
            except TypeError:
                for col in range(2,5):
                    [last] = collections.deque(old_timetable, maxlen=1)
                    value = self.sheet.cell(row=i, column=col).value
                    if col == 2:
                        old_timetable[last]['time'] = value
                        schedule[-1].time = value

                    elif col == 3:
                        old_timetable[last]['type'],old_timetable[last]['name_subject'] = str(value).split(' ',maxsplit=1)
                        schedule[-1].type, schedule[-1].name_subject = str(value).split(' ',maxsplit=1)
                    elif col == 4:
                        val = str(value).split("\n")
                        old_timetable[last]['name_teacher'] = val[0]
                        old_timetable[last]['auditory'] = val[1].split()[1]
                        #old_timetable[last]['faculty'] = faculty[random.randint(0,1)]

                        schedule[-1].name_teacher = val[0]
                        schedule[-1].auditory = val[1].split()[1]


        self.output_data = schedule

    # def parse_name_group(self, full_path):
    #     name_group = full_path[full_path.find('(') + 1: full_path.find(',')]
    #     information_group = []
    #     information_group.append(name_group.split('-')[0])
    #     self.spec = name_group.split('-')[0]
    #     self.course = name_group.split('-')[1][0]
    #     self.number = name_group.split('-')[1][1:]
    #     self.sheet = self.__file.active
    #     self.output_data = []