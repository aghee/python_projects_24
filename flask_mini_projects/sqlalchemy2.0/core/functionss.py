from sqlalchemy.sql import func,select 
from main import engine,studnts,addresses,reflected_table

'''
Standard SQL has recommended many functions which are implemented by most dialects.
The func keyword in SQLAlchemy API is used to generate these functions.
'''
'''
#now()- returns current date and time
stmt=select(func.now())
with engine.connect() as conn:
    result=conn.execute(stmt)
    print(result.fetchone())
'''
'''
#count()- returns number of rows selected from a table
stmt=select(func.count(addresses.c.id))
with engine.connect() as conn:
    result=conn.execute(stmt)
    print(result.fetchone())
'''
'''
#max()
#column names are case sensitive
stmt=select(func.max(reflected_table.c.AGE))
with engine.connect() as conn:
    result=conn.execute(stmt)
    print(result.fetchone())
'''
'''
#min()
stmt=select(func.min(reflected_table.c.SALARY).label('minimum_wage'))
with engine.connect() as conn:
    result=conn.execute(stmt)
    print(result.fetchone())
'''
#avg()
# stmt=select(func.avg(reflected_table.c.SALARY).label('average_salary'))
stmt=select(func.avg(reflected_table.c.AGE).label('average_age'))
with engine.connect() as conn:
    result=conn.execute(stmt)
    print(result.fetchone())
