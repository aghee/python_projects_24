from sqlalchemy import create_engine,ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import Flask,render_template


Base=declarative_base()
app=Flask(__name__)
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

class Thing(Base):
    __tablename__='thingtable'

    thingid=Column('thingid',Integer,primary_key=True)
    desc=Column('description',String)
    owner=Column(Integer,ForeignKey('people.ssn'))

    def __init__(self,thingid,desc,owner):
        self.thingid=thingid
        self.desc=desc
        self.owner=owner

    def __repr__(self):
        return f'{self.thingid} {self.desc} owned by {self.owner}'


engine=create_engine('sqlite:///mydb.db', echo=True)
#echo=True--when set to true makes the engine log all the 
#sql statements it executes-useful for debugging
Base.metadata.create_all(bind=engine)#connects to the engine and converts classes to db tables

Session=sessionmaker(bind=engine)
session=Session()

# person=Person(5555,'agy','mutembei','F',26)
# session.add(person)
# session.commit()

# p1=Person(554,'zane','beina','M',39)
# p2=Person(553,'kibs','musqa','M',261)
# p3=Person(552,'agyness','muremi','F',12)
# p4=Person(551,'april','mutamu','m',45)
# p5=Person(555,'zalika','shulwe','F',59)
# p7=Person(199,'Grapes','Sweet','Unknown',14)

# t1=Thing(600,'sofaset',p1.ssn)
# t2=Thing(601,'utensils',p1.ssn)
# t3=Thing(602,'laundrymachine',p2.ssn)
# t3=Thing(603,'laundrymachine',p5.ssn)

# session.add(p1)
# session.add(p2)
# session.add(p3)
# session.add(p4)
# session.add(p5)
# session.add(p7)

# session.add(t1)
# session.add(t2)
# session.add(t3)
# session.add(t3)
# session.commit()

# results=session.query(Person).filter(Person.lastname.like('%mu%'))
@app.route('/display')
def display():
    results=session.query(Person).all()
    return render_template('index.html',results=results)
# thing_results=session.query(Thing,Person).filter(Thing.owner==Person.ssn).filter(Person.firstname.like('%za%')).all()
# print(results)
# for i in results:
#     print(i)
if __name__=='__main__':
    app.run(debug=True)