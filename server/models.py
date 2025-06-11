from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String,MetaData

metadata = MetaData()
# base class
db = SQLAlchemy(metadata=metadata)
class Student(db.Model):
    __tablename__= "students"

    id = Column(Integer(),primary_key=True)
    name = Column(String(80),nullable=False)

class Course(db.Model):
    __tablename__ = "courses"

    id = Column(Integer(),primary_key=True)
    name = Column(String())