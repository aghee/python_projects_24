from main import students,addresses,engine

#Syntax: table.update().where(conditions).values(SET expressions)
'''
output1=students.update().where(students.c.lname.like('%end%')).values(lname='weekend')
# output1=students.update().where(students.c.lname=='mutembei').values(lname='monzee')
conn= engine.connect()
conn.execute(output1)
# conn.commit()
result=students.select()
updated_records=conn.execute(result).fetchall()
print(updated_records)

'''
# output2=result.fetchall()
# print(output2)

#Update multiple tables at once
stmt = students.update().\
values({
   students.c.first_name:'xyz',
   addresses.c.email_add:'abc@xyz.com'
}).\
where(students.c.id == addresses.c.st_id)
with engine.connect() as conn:
    result=conn.execute(stmt)
    conn.commit()