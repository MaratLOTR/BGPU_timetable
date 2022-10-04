FROM python:3.9
VOLUME C:/Домашняя работа/Управление проектами/schedule_excel
#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt
#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#
COPY ./src /code/app

#
WORKDIR /code/app
CMD ["python3", "main.py"]

