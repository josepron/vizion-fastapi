from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from config.db import meta, engine

orders = Table("orders", meta, 
               Column('id', Integer, primary_key=True),
               Column('date', DateTime),
               Column('phone', String(50)),
               Column('prepayment', String(50)))

meta.create_all(engine)