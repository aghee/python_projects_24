from sqlalchemy import insert
from tables import users_table
from connect1 import engine

# stmt=insert(users_table).values(name='tuesady',fullname='asali siri')
stmt=insert(users_table)
list_vals=[
    {'name':'kulima','fullname':'wednesday again'},
    {'name':'casidy','fullname':'casandara melody'},
    {'name':'bluey','fullname':'Bluey family'}
]

with engine.connect() as conn:
    conn.execute(stmt,list_vals)
    conn.commit()

print(stmt)