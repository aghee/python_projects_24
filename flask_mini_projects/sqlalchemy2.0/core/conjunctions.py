'''
Conjunctions- functions in SQLAlchemy that implement relational
operators used in WHERE clause of SQL expressions.The operators 
AND, OR, NOT, etc., are used to form a compound expression 
combining two individual logical expressions
'''
from sqlalchemy import and_,or_,asc,desc,between
from main import studnts,engine
from sqlalchemy.sql import select

'''
#AND
# stmt=select(studnts).where(and_(studnts.c.first_name.startswith('xyz'),studnts.c.id<8))
stmt=select(studnts).where(and_(studnts.c.first_name.like('%a%'),studnts.c.id<8))
with engine.connect() as conn:
    result=conn.execute(stmt)
    final_data_set=result.fetchall()
    print(final_data_set)

'''
'''
#OR
stmt=select(studnts).where(or_(studnts.c.first_name=='Rav',studnts.c.id<=3))
with engine.connect() as conn:
    result=conn.execute(stmt)
    final_data_set=result.fetchall()
    print(final_data_set)
'''
'''
# order_by asc,desc
# stmt=select(studnts).order_by(asc(studnts.c.lname))
stmt=select(studnts).order_by(desc(studnts.c.lname))
with engine.connect() as conn:
    result=conn.execute(stmt)
    for i in result:
        print(i)
'''
#between -is inclusive of range start and end
stmt=select(studnts).where(between(studnts.c.id,1,4))
with engine.connect() as conn:
    result=conn.execute(stmt)
    for i in result:
        print(i)