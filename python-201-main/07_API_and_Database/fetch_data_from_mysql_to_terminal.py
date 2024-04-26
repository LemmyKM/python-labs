import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/file_counter')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
file_count = sqlalchemy.Table('file_count', metadata, autoload_with=engine)

query = sqlalchemy.select(file_count)
result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()
pprint(result_set)