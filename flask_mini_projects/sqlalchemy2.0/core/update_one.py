from main import students,engine

#Syntax: table.update().where(conditions).values(SET expressions)

output1=students.update().where(students.c.lname.like('%end%')).values(lname='weekend')
# output1=students.update().where(students.c.lname=='mutembei').values(lname='monzee')
conn= engine.connect()
conn.execute(output1)
# conn.commit()
result=students.select()
updated_records=conn.execute(result).fetchall()
print(updated_records)


# output2=result.fetchall()
# print(output2)