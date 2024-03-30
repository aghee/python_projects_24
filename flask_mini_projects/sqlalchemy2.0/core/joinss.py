from main import studnts,addresses,engine
from sqlalchemy import text,join
from sqlalchemy.sql import select

'''
Syntax: join(right, onclause = None, isouter = False, full = False)
where : right − the right side of the join; this is any Table object
        onclause − a SQL expression representing the ON clause of the join.
        If left at None, it attempts to join the two tables based on a foreign key relationship
        isouter − if True, renders a LEFT OUTER JOIN, instead of JOIN
        full − if True, renders a FULL OUTER JOIN, instead of LEFT OUTER JOIN
'''
'''
# print(studnts.join(addresses))
#INNER_JOIN
table_from_join=studnts.join(addresses)
table_from_join1=table_from_join.select().where(addresses.c.postal_add.like('%te%'))
with engine.connect() as conn:
    result=conn.execute(table_from_join1)
    join_result=result.fetchall()
    print(join_result)
'''
'''
#LEFT JOIN
#FOR RIGHT JOIN- JUST POSITION THE TABLE BASED ON RESULT YOU WANT
table_from_join=studnts.join(addresses,isouter=True)
table_from_join1=table_from_join.select()
with engine.connect() as conn:
    result=conn.execute(table_from_join1)
    # join_result=result.fetchall()
    # print(join_result)
    for i in result:
        print(i)
'''
'''
#FULL JOIN- ***FAILED TO EXECUTE***
table_from_join=studnts.outerjoin(addresses,studnts.c.id==addresses.c.st_id)
table_from_join1=select([studnts,addresses]).select_from(table_from_join)
with engine.connect() as conn:
    result=conn.execute(table_from_join1)
    join_result=result.fetchall()
    print(join_result)
'''
'''
#INNER JOIN-***FAILED***
table_from_join=studnts.join(addresses,studnts.c.id==addresses.c.st_id)
table_from_join1=select([studnts]).select_from(table_from_join)
with engine.connect() as conn:
    result=conn.execute(table_from_join1)
    join_result=result.fetchall()
    print(join_result)
'''