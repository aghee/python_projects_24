from sqlalchemy import Column,Integer,String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine=create_engine('mysql+pymysql://root:pythonsql1@localhost/testdb_one',echo=None)
Base=declarative_base()

class Customers(Base):
    __tablename__='customers'

    # def __init__(self,fname,lname,email_add):
    #     self.fname=fname
    #     self.last_name=lname
    #     self.email_address=email_add
        
    id=Column(Integer,primary_key=True)
    fname=Column(String(25),nullable=False)
    # mid_name=Column(String(25),nullable=True)
    last_name=Column(String(30),nullable=False)
    email_address=Column(String(30),nullable=False)

Base.metadata.create_all(engine)