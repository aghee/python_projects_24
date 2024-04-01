from creating_sessions import session
from declaring_mapping import Customers

# object_with_id2=session.query(Customers).get(5) #legacy/outdated
object_with_id2=session.get(Customers,5)
# print('Name:',object_with_id2.fname,'Lastname:',object_with_id2.last_name,'Email:',object_with_id2.email_address)
object_with_id2.email_address='k254kl@zoomail.co.ke' #update email_address with new value
session.commit()
# print(object_with_id2.email_address)
first_obj=session.query(Customers).first()
# print(first_obj.fname,first_obj.last_name)
first_obj.fname='Updatedfname quiks'
# print(first_obj.fname)
session.rollback()
# print(first_obj.fname)
# session.commit()

#bulk update
updated_rec=session.query(Customers).filter(Customers.id !=2).update({Customers.fname:'Mr.' + Customers.fname},synchronize_session=False)
session.commit()
# session.rollback()
print('number of records updated:',updated_rec)
'''
update() takes two parameters
-A dictionary of key-values with key being the attribute to be updated,
and value being the new contents of attribute.
-synchronize_session attribute mentioning the strategy to update attributes
in the session. Valid values are false: for not synchronizing the session,
fetch: performs a select query before the update to find objects that are 
matched by the update query; and evaluate: evaluate criteria on objects in the session

'''