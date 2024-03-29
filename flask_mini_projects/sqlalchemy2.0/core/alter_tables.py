from main import engine
from sqlalchemy import text

with engine.connect() as conn:
    result=text('alter table addresses modify column postal_add varchar(30)')
    conn.execute(result)
    conn.commit()