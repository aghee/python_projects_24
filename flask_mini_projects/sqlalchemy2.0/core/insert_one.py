from main import engine,studnts,testtable1,addresses

# insert one item
# ins=studnts.insert().values(fname='village',lname='market')
insert1=testtable1.insert().values(dob='31-01-24',status='marrd',home_town='kiambu',occupation='dokey')
insert2=addresses.insert()
# print(str(ins))
# print(ins.compile().params)
#insert many items
list_of_values=[{'fname':'Rajiv', 'lname' : 'Khanna'},
   {'fname':'Komal','lname' : 'Bhandari'},
   {'fname':'Abdul','lname' : 'Sattar'},
   {'fname':'Priya','lname' : 'Rajhans'},]
list_of_addresses=[
    {'st_id':1,'email_add':'stud1@yahoo.com','postal_add':'kilimani254'},
     {'st_id':1, 'postal_add':'ChurchGate Mumbai', 'email_add':'kapoor@gmail.com'},
   {'st_id':3, 'postal_add':'Jubilee Hills Hyderabad', 'email_add':'komal@gmail.com'},
   {'st_id':5, 'postal_add':'MG Road Bangaluru', 'email_add':'as@yahoo.com'},
   {'st_id':2, 'postal_add':'Cannought Place new Delhi', 'email_add':'admin@khanna.com'},
]

with engine.connect() as conn:
   #  result=conn.execute(ins) #result represents Resultproxy
    result=conn.execute(insert2,list_of_addresses)
    #insert many items at once
    # result=conn.execute(studnts.insert(),list_of_values)
    conn.commit()

