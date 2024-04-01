from creating_sessions import session
from declaring_mapping import Customers
'''
#Add a single record
# obj1=Customers('kazika','kalehana','kazekale@gmail.com')
obj1=Customers('indomie','slices','naivas@gmail.com')
session.add(obj1)
session.commit()
'''

'''
#print(dir(session)) #displays all attributes and methods of session
#check for a particular method/attribute
if 'add_all_' in dir(session):
    print('Found!')
else:
    print('not found!')
'''
#To add multiple records
session.add_all([
    # Customers(fname='santa maria',last_name='spaghetti',email_address='smghte@gmail.com'),
    # Customers(fname='santa lucia',last_name='noodles',email_address='slucianood@gmail.com'),
    Customers(fname='nuvita',last_name='cookies',email_address='nuvcooks@gmail.com'),
    Customers(fname='nuvita',last_name='biscuits',email_address='nuvbics@gmail.com')
    ] 
)
session.commit()