from tables import users_table
from connect1 import engine
from sqlalchemy import select

stmt=select(users_table).where(users_table.c.name.like('%y'))
with engine.connect() as conn:
    result=conn.execute(stmt)
    # print(result.fetchall())
    for i in result:
        print(f'<username={i.name} fullname={i.fullname}>')

# print(stmt)
# print(users_table.c.fullname)