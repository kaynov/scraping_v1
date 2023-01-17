import databases
from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, ForeignKey, create_engine, \
    func, select, Date, insert, Float
from datetime import datetime, date
import psycopg2


metadata = MetaData()

comps = Table(
    "comps",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("items_name", String, index=True),
    Column("items_link", String, index=True),
    Column("price", Float),
    Column("rate", Float),
    Column("create_date", Date, default=datetime.now())
)


engine = create_engine('postgresql://postgres:s1t@localhost/test_1')
metadata.create_all(engine)


conn = engine.connect()
ins = insert(comps)

# r = conn.execute(ins,
#     items_name="test2",
#     price=123,
#     rate=1
#     )

