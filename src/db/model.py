from sqlalchemy import Integer, String, \
    Column, DateTime
from db.database import Base


class Schedule(Base):
    __tablename__ = 'schedule'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_group = Column(String)
    type = Column(String(10), nullable=False)
    name_subject = Column(String(200), nullable=False)
    name_teacher = Column(String(50), nullable=False)
    auditory = Column(String(200), nullable=False)
    time = Column(String)
    date = Column(DateTime)
#
# if __name__ == '__main__':
#     Base.metadata.create_all(engine)
