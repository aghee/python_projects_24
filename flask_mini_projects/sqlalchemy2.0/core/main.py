from sqlalchemy import create_engine
from sqlalchemy import Table,Column,Integer,String,MetaData

# engine=create_engine('mysql+pymysql://root:pythonsql1@localhost/testdb_one',echo=True)
engine=create_engine('sqlite:///students.db',echo=True)
metaobj=MetaData()

students=Table(
    'students',
    metaobj,
    Column('id',Integer,primary_key=True),
    Column('fname',String(25)),
    Column('lname',String(40))
)

#create table in db if does not already exist
metaobj.create_all(engine)

