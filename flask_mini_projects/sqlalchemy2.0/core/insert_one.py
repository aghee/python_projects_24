from main import engine,students

# insert one item
ins=students.insert().values(fname='village',lname='market')
print(str(ins))
print(ins.compile().params)

#insert many items
list_of_values=[{'fname':'Rajiv', 'lname' : 'Khanna'},
   {'fname':'Komal','lname' : 'Bhandari'},
   {'fname':'Abdul','lname' : 'Sattar'},
   {'fname':'Priya','lname' : 'Rajhans'},]

with engine.connect() as conn:
    result=conn.execute(ins) #result represents Resultproxy
    #insert many items at once
    # result=conn.execute(students.insert(),list_of_values)
    conn.commit()

