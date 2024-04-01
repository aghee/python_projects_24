from sqlalchemy.orm import sessionmaker
from declaring_mapping import engine

Session=sessionmaker(bind=engine)
session=Session()