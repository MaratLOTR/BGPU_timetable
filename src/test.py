from requests import get, post

query = post("https://isu.ugatu.su/api/new_schedule_api/?schedule_semestr_id=222&WhatShow=1&student_group_id=1631&weeks=36")
with open('html_example.txt', 'a') as f:
    f.write(query.content.decode('utf-8'))