import sqlalchemy


engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/bloeddruk')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

# table:
bd = sqlalchemy.Table('bd', metadata, autoload_with=engine)

query = sqlalchemy.insert(bd).values(sys=125, dia=101, pulse=75)
result_proxy = connection.execute(query)
connection.commit()
connection.close()