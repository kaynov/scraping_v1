import databases
from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, ForeignKey, create_engine, \
    func, select, Date
from datetime import datetime, date

metadata = MetaData()

comps = Table(
    "comps",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("items_name", String, index=True),
    Column("price", Integer),
    Column("rate", Integer),
    Column("create_date", Date, default=datetime.now())
)
