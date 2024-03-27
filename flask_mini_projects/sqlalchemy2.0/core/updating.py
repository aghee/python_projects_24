from tables import users_table
from sqlalchemy import update
from connect1 import engine

stmt=update(users_table).where(users_table.c.name =='kulima').values(name='kunsiiima')
print(stmt)
with engine.connect() as conn:
    result=conn.execute(stmt)
    conn.commit()