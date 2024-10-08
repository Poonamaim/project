import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="NEELAM10$",
  database="mydb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT personid, email FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)