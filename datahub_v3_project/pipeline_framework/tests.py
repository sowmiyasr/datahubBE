import psycopg2

connection = psycopg2.connect(user="postgres",
                                  password="datahub123",
                                  host="localhost",
                                  port="5432",
                                  database="framework")

cursor = connection.cursor()

postgres_insert_query = """ INSERT INTO logs(name) VALUES (%s)"""
record_to_insert = ('success',)
#print('connection successfully')
cursor.execute(postgres_insert_query, record_to_insert)
connection.commit()