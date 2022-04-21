# Web server
from sqlalchemy import ForeignKey, create_engine


db_string= "postgresql://root:root@localhost:5432/store"

engine = create_engine(db_string)
connection = engine.connect()

# #create
#connection.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")
#connection.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")

#tp 
#2.1
with open ("src/create_table.sql", "r") as create_table :
    # print(create_table.read())
    connection.execute(create_table.read())

# file = open("")  mais avec with pas besoin de close le fichier
# file.read()
# file.close()

#2.2 



