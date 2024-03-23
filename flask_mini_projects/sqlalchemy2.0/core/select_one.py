from main import students,engine
from sqlalchemy import text

#select -read-only-must not have commit()
selected_item=students.select()
# print(repr(selected_item))
# print(str(selected_item))
with engine.connect() as conn:
    result=conn.execute(selected_item)#result represents ResultProxy
    #where clause, c is an alias for column
    #idgreaterfour=students.select().where(students.c.id>11)
    # result=conn.execute(idgreaterfour)
    t=text('select * from students')
    result=conn.execute(t)
    conn.commit()
#result.fetchall()- any fetch() represents resultset
#print(result.inserted_primary_key)

#displays all selected rows in a table-tuples in a list
row=result.fetchall() #fetchone-returns first record only
print(row)

#display all selected rows in the table
for record in result:
    print(record)

'''
#alias- unable to use alias
from sqlalchemy import create_engine
from sqlalchemy.sql import alias,select

engine=create_engine('sqlite:///students.db',echo=True)
conn=engine.connect()
st=students.alias('a')
s=select([st]).where(st.c.id>5) 

conn.execute(s).fetchall()

'''