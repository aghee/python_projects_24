from main import engine,addresses
from sqlalchemy import union,union_all,except_,intersect
from sqlalchemy.sql import select

'''
#union()-***this code still gives duplicates -WHY??***
#eliminates duplicates from the resultset
# The number of columns and datatype must be same in both the tables.
stmt=union(select(addresses).where(addresses.c.email_add.like('%@gmail.com')),\
select(addresses).where(addresses.c.email_add.like('%yahoo.com')))
with engine.connect() as conn:
    result=conn.execute(stmt)
    print(result.fetchall())
'''
'''
#union_all()
#cannot remove the duplicates and cannot sort the data in the resultset
stmt=union_all(select(addresses).where(addresses.c.email_add.like('%@gmail.com')),\
select(addresses).where(addresses.c.email_add.like('%yahoo.com')))
with engine.connect() as conn:
    result=conn.execute(stmt)
    # print(result.fetchall())
    for i in result:
        print(i)
'''
'''
#except_()
#combine two SELECT statements and return rows from the first SELECT statement 
#that are not returned by the second SELECT statement.
stmt=except_(select(addresses).where(addresses.c.email_add.like('%gmail%')),\
    select(addresses).where(addresses.c.postal_add.like('%est')))
with engine.connect() as conn:
    result=conn.execute(stmt)
    print(result.fetchall())
'''
#intersect()
#Using INTERSECT operator, SQL displays common rows from both the SELECT statements
stmt=intersect(select(addresses).where(addresses.c.email_add.like('%gmail%')),\
    select(addresses).where(addresses.c.postal_add.like('%est')))
with engine.connect() as conn:
    result=conn.execute(stmt)
    # print(result.fetchall())
    for i in result:
        print(i)
