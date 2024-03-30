from main import studnts,addresses,engine

#Syntax: table.update().where(conditions).values(SET expressions)
'''
output1=studnts.update().where(studnts.c.lname.like('%end%')).values(lname='weekend')
# output1=studnts.update().where(studnts.c.lname=='mutembei').values(lname='monzee')
conn= engine.connect()
conn.execute(output1)
# conn.commit()
result=studnts.select()
updated_records=conn.execute(result).fetchall()
print(updated_records)

'''
# output2=result.fetchall()
# print(output2)

#Update multiple tables at once
stmt = studnts.update().\
values({
   studnts.c.first_name:'xyz',
   addresses.c.email_add:'abc@xyz.com'
}).\
where(studnts.c.id == addresses.c.st_id)
with engine.connect() as conn:
    result=conn.execute(stmt)
    conn.commit()