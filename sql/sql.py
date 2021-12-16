import mysql.connector

my_server = mysql.connector.connect(
  host="localhost",
  user="root",
  password="hesoyam@SA26"
)

my_cursor = my_server.cursor(buffered=True)

my_cursor.execute("show databases")

my_cursor.execute("use sakila")

my_cursor.execute("select * from actor where actor_id <= 10")

for record in my_cursor:
	print(record)