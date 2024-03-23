from main import students,engine,testtable1
from sqlalchemy.sql import text

conn=engine.connect()
del_output=testtable1.delete().where(testtable1.c.occupation.like('%k%'))
result=conn.execute(del_output)
conn.commit()
# updated_table=testtable1.select()
# finaltable=conn.execute(updated_table)

# result=text('DROP TABLE testtable1')
# conn.execute(result)
# tablecheck=testtable1.select()
# showtable=conn.execute(tablecheck)



