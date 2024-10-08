import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database ="mydb"
)

mycursor = mydb.cursor()
if(mycursor):
    print("connected sucessfully")

