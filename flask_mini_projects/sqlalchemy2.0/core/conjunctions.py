'''
Conjunctions- functions in SQLAlchemy that implement relational
operators used in WHERE clause of SQL expressions.The operators 
AND, OR, NOT, etc., are used to form a compound expression 
combining two individual logical expressions
'''
from sqlalchemy import and_,or_,asc,desc,between
from main import students,engine
from sqlalchemy.sql import select

'''
#AND
# stmt=select(students).where(and_(students.c.first_name.startswith('xyz'),students.c.id<8))
stmt=select(students).where(and_(students.c.first_name.like('%a%'),students.c.id<8))
with engine.connect() as conn:
    result=conn.execute(stmt)
    final_data_set=result.fetchall()
    print(final_data_set)

'''
'''
#OR
stmt=select(students).where(or_(students.c.first_name=='Rav',students.c.id<=3))
with engine.connect() as conn:
    result=conn.execute(stmt)
    final_data_set=result.fetchall()
    print(final_data_set)
'''
'''
# order_by asc,desc
# stmt=select(students).order_by(asc(students.c.lname))
stmt=select(students).order_by(desc(students.c.lname))
with engine.connect() as conn:
    result=conn.execute(stmt)
    for i in result:
        print(i)
'''
#between -is inclusive of range start and end
stmt=select(students).where(between(students.c.id,1,4))
with engine.connect() as conn:
    result=conn.execute(stmt)
    for i in result:
        print(i)