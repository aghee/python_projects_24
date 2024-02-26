from sqlalchemy import create_engine,ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base=declarative_base()

class Person(Base):
    __tablename__="people"

    ssn=Column("ssn",Integer,primary_key=True)
    firstname=Column("firstname",String)
    lastname=Column("lastname",String)
    gender=Column("gender",CHAR)
    age=Column("age",Integer)

    def __init__(self,ssn,fname,lname,gender,age):
        self.ssn=ssn
        self.firstname=fname
        self.lastname=lname
        self.gender=gender
        self.age=age

    def __repr__(self):
        return f'({self.ssn}) {self.firstname} {self.lastname} ({self.gender},{self.age})'

engine=create_engine('sqlite:///mydb.db', echo=True)
Base.metadata.create_all(bind=engine)

Session=sessionmaker(bind=engine)
session=Session()

person=Person(5555,'agy','mutembei','F',26)
session.add(person)
session.commit()

p1=Person(554,'zane','beina','M',39)
p2=Person(553,'kibs','musqa','M',261)
p3=Person(552,'agyness','muremi','F',12)
p4=Person(551,'april','mutamu','m',45)

session.add(p1)
session.add(p2)
session.add(p3)
session.add(p4)

session.commit()
