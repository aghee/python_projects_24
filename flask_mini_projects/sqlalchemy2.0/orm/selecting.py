from declaring_mapping import Customers
from creating_sessions import session

'''
Syntax
selected_records=session.query(mappedClass)
selected_records=Query(mappedClass,session)-***FAILS TO EXECUTE***
#print(dir(session.query(Customers))) #View all methods and attributes of the query object
'''
#The result variable will contain a list of instances of the Customers class.
#Each instance will have attributes corresponding to the columns of the Customers table.
#These instances are objects, not dictionaries or tuples.
result=session.query(Customers).all()
# result=session.query(Customers).one()
# r=session.query(Customers).filter(Customers.id==3).scalar()
# print(r.fname)
# result=query(Customers,session)#***FAILS TO EXECUTE***
# print(result)
for customer_obj in result:
    print('Firstname:',customer_obj.fname,'Lastname:',customer_obj.last_name,'email:',customer_obj.email_address)
'''
Returning lists and scalars
all() returns a list
first() applies a limit of one and returns the first result as a scalar.
The bound parameters for LIMIT is 1 and for OFFSET is 0
This command fully fetches all rows, and if there is not exactly one object
identity or composite row present in the result, it raises an error
scalar-invokes the one() method, and upon success returns the first column of the row
'''
