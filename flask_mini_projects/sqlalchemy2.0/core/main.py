from sqlalchemy import create_engine
from sqlalchemy import Table,Column,Integer,String,MetaData,Float

engine=create_engine('mysql+pymysql://root:pythonsql1@localhost/testdb_one',echo=None)
# engine=create_engine('sqlite:///testdb_one.db',echo=True)
metaobj=MetaData()

students=Table(
    'students',
    metaobj,
    Column('id',Integer,primary_key=True),
    Column('first_name',String(25)),
    Column('lname',String(40)),
    Column('marks',Integer),
    Column('fin_gpa',String(25)),
    Column('comments',String(30)),
    Column('salary',Float)   
)

testtable1=Table(
    'testtable1',
    metaobj,
    Column('dob',String(9)),
    Column('status',String(12)),
    Column('home_town',String(25)),
    Column ('occupation',String(25))

)
#create table in db if does not already exist
metaobj.create_all(engine)


