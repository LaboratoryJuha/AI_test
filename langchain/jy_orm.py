from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:1234@localhost:4456/postgres")


# row 방식
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


# core 방식
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

# metadata = MetaData()

# sample_table = Table(
#     "sample_table",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String(30)),
# )

# print(sample_table.c.name)
# print(repr(sample_table.c.name))
# print(sample_table.c.keys())

# metadata.create_all(engine)


# orm 방식
from sqlalchemy.orm import registry, sessionmaker   

mapper_registry = registry()

print(mapper_registry.metadata)
base = mapper_registry.generate_base()

class SampleTable(base):
    __tablename__ = "sample_table"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))

    def __repr__(self):
        return f"SampleTable(id={self.id}, name={self.name})"

SampleTable.__table__

mapper_registry.metadata.create_all(engine)
base.metadata.create_all(engine)

session  = sessionmaker(bind=engine)
session = session()

test = SampleTable(id=1, name="first")
print(test)

session.add(test)
session.commit()

sample_table = Table( "sample_table", metadata, autoload_with=engine)
print(sample_table)

