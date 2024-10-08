import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="NEELAM10$",
  database="mydb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (personid,StudentName,firstName,age,email,mobile) VALUES (%s, %s,%s,%s,%s,%s)"
val = (1,"John", "Highway", 21,"joohan@gmail",98756434)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")