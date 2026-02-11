from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:1234@localhost:4456/postgres")


#from sqlalchemy import text
#
#with engine.connect() as conn:
#    result = conn.execute(text("SELECT version();"))
#    print(result.fetchone())
#
#query = """
#CREATE EXTENSION IF NOT EXISTS vector;
#CREATE TABLE IF NOT EXISTS items (
#    id SERIAL PRIMARY KEY,
#    embedding vector(768)
#);"""
#with engine.connect() as conn:
#    result = conn.execute(text(query))
#    conn.commit()

from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()


sample_table = Table(
    "sample_table",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
)


print(sample_table.c.name)
print(sample_table.c.keys())

