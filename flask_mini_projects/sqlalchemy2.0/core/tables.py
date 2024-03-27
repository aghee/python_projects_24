from sqlalchemy import MetaData
from sqlalchemy import Table,Column,Integer,String,Text,ForeignKey

"""
    users table:
       -id pk
       -name str
       -fullname str
       -email

    comments table:
        -id pk
        -comment str
        -user_id int>users.id

"""
metaobj=MetaData()
users_table=Table(
    'users',
    metaobj,
    Column('id',Integer,primary_key=True),
    Column('name',String(25),nullable=False),
    Column('fullname',Text)
)

comments_table=Table(
    'comments',
    metaobj,
    Column('id',Integer,primary_key=True),
    Column('comment',Text,nullable=False),
    Column('user_id',ForeignKey('users.id'))
)