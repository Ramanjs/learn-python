import mysql.connector

# connecting to server
my_server = mysql.connector.connect(
	host="localhost",
	user="root",
	password="hesoyam@SA26",
	database="sakila"
	)

my_cursor = my_server.cursor()

my_cursor.execute("select first_name from actor")

my_result = my_cursor.fetchall() # returns a list of rows

for row in my_result:
	print(row)

# pip install mysql-connector-python
# mysql.connector.connect
# .cursor()
# .execute()
# .commit() -> to save
# fetchall()