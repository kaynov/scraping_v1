from sqlalchemy import MetaData, Table, String, Integer, Column, create_engine, Date, insert, Float
from datetime import datetime


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


