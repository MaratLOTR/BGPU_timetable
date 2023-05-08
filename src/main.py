from fastapi import FastAPI
import uvicorn
from routers import group, filter_group, teacher_filter

app = FastAPI()
app.include_router(group.router)
app.include_router(filter_group.router)
app.include_router(teacher_filter.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


# from parser_excel.main_parser import start_parser
#
#
# if __name__ == '__main__':
#     start_parser('C:/Домашняя работа/Управление проектами/schedule_excel')