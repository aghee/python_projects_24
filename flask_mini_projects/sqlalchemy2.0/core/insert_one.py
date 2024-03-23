from main import engine,students,testtable1

# insert one item
# ins=students.insert().values(fname='village',lname='market')
insert1=testtable1.insert().values(dob='31-01-24',status='marrd',home_town='kiambu',occupation='dokey')
# print(str(ins))
# print(ins.compile().params)
#insert many items
list_of_values=[{'fname':'Rajiv', 'lname' : 'Khanna'},
   {'fname':'Komal','lname' : 'Bhandari'},
   {'fname':'Abdul','lname' : 'Sattar'},
   {'fname':'Priya','lname' : 'Rajhans'},]

with engine.connect() as conn:
   #  result=conn.execute(ins) #result represents Resultproxy
    result=conn.execute(insert1)
    #insert many items at once
    # result=conn.execute(students.insert(),list_of_values)
    conn.commit()

