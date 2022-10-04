import openpyxl
from datetime import datetime
import collections
import db.model as model


class Parser:
    def __init__(self, full_path: str):
        self.__excel_file = openpyxl.load_workbook(full_path)
        self.name_group = full_path[full_path.find('(')+1 : full_path.find(',')]
        self.sheet = self.__excel_file.active

    def parse(self):
        length = self.sheet.max_row
        timetable = {}
        schedule = []
        for i in range(2, length + 1):
            value = self.sheet.cell(row=i, column=1).value
            try:
                date = datetime.strptime(value, "%d.%m.%Y")
                timetable[date] = {}
                schedule.append(model.Schedule(date=date))
            except TypeError:
                for col in range(2,5):
                    [last] = collections.deque(timetable, maxlen=1)
                    value = self.sheet.cell(row=i, column=col).value
                    if col == 2:
                        timetable[last]['time'] = value
                        schedule[-1].time = value
                        schedule[-1].name_group = self.name_group
                    elif col == 3:
                        timetable[last]['type'],timetable[last]['name_subject'] = str(value).split(' ',maxsplit=1)
                        schedule[-1].type, schedule[-1].name_subject = str(value).split(' ',maxsplit=1)
                    elif col == 4:
                        val = str(value).split("\n")
                        timetable[last]['name_teacher'] = val[0]
                        timetable[last]['auditory'] = val[1].split()[1]

                        schedule[-1].name_teacher = val[0]
                        schedule[-1].auditory = val[1].split()[1]
        return schedule