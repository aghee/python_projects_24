from main import studnts,addresses,engine
from sqlalchemy import text
from sqlalchemy.sql import select

#***Do NOT use [] in select()***
selected_studnts=select(studnts,addresses).where(studnts.c.id==addresses.c.st_id)
with engine.connect() as conn:
    result=conn.execute(selected_studnts)
    final_result=result.fetchall()
    print(final_result)
    # selected_qry=text('select s.id,s.first_name,s.lname,a.st_id from studnts s, addresses a where s.id=a.st_id')
    # final_selected_qry=conn.execute(selected_qry)
    # final_selected=final_selected_qry.fetchall()
    # print(final_selected)

'''
#select -read-only-must not have commit()
selected_item=studnts.select()
# print(repr(selected_item))
# print(str(selected_item))
with engine.connect() as conn:
    result=conn.execute(selected_item)#result represents ResultProxy
    #where clause, c is an alias for column
    #idgreaterfour=studnts.select().where(studnts.c.id>11)
    # result=conn.execute(idgreaterfour)
    t=text('select * from studnts')
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

#alias- unable to use alias
from sqlalchemy import create_engine
from sqlalchemy.sql import alias,select

engine=create_engine('sqlite:///studnts.db',echo=True)
conn=engine.connect()
st=studnts.alias('a')
s=select([st]).where(st.c.id>5) 

conn.execute(s).fetchall()
'''