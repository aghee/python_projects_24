from connect1 import engine
from tables import metaobj,users_table,comments_table

print('>>>DB CREATED')
metaobj.create_all(bind=engine)