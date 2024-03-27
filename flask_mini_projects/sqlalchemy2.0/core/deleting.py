from tables import users_table
from sqlalchemy import delete
from connect1 import engine

stmt=delete(users_table).where(users_table.c.id==2)
print(stmt)
with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()