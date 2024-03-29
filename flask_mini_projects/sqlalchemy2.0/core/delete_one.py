from main import students,addresses,engine,testtable1
from sqlalchemy.sql import text

'''
del_output=testtable1.delete().where(testtable1.c.occupation.like('%ed'))
with engine.connect() as conn:
    result=conn.execute(del_output)
    conn.commit()
'''
    # updated_table=testtable1.select()
# finaltable=conn.execute(updated_table)

# result=text('DROP TABLE testtable1')
# conn.execute(result)
# tablecheck=testtable1.select()
# showtable=conn.execute(tablecheck)

#DELETE FROM MULTIPLE TABLES AT ONCE
stmt=addresses.delete().\
    where(students.c.id==addresses.c.st_id).\
    where(addresses.c.email_add.startswith('xyz%'))
with engine.connect() as conn:
    deleted_rec=conn.execute(stmt)
    conn.commit()



