import psycopg2
from auth import dbname,host,password,port,user

class Database:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname='%s' user='%s' host='%s' password='%s' port='%s'"
                %(dbname,user,host,password,port))
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pprint("Failure in connection")
        try:
            create_table_command = ("CREATE TABLE tweet(id serial PRIMARY KEY, id_twitter varchar(50),\
             name varchar(500), text varchar(500), image varchar(300), followers integer, location varchar(100),\
             classification varchar(216));")
            self.cursor.execute(create_table_command)
            print('Table created')
        except:
            pass

    def insert_new(self,id_twitter, name, text, image, followers, location, classification):
        insert_command = ("INSERT INTO tweet(id_twitter, name, text, image, followers, location, classification)\
         VALUES('%s','%s','%s','%s','%d','%s','%s')" 
        %(id_twitter, name, text, image, followers, location,classification))
        self.cursor.execute(insert_command)
