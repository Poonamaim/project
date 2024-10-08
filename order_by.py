import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="NEELAM10$",
  database="mydb"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY email"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)