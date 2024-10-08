import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="NEELAM10$",
  database="mydb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (personid,StudentName,firstName,age,email,mobile) VALUES (%s, %s,%s,%s,%s,%s)"

val = [
  (2,'Peter', 'Lowstreet ',4,'peter@gmail',9065575),
  (3,'Amy', 'Apple st', 6,'amy@gmail.com',455609),
  (4,'Hannah', 'Mountain', 21,'hannah@.com',345678),
  (5,'Michael', 'Valley', 3,'michael@com',45675),
  (6,'Sandy', 'Ocean blvd', 2,'sandy@gmaail',456743),
  (7,'Betty', 'Green Grass', 12,'betty@gmail',34567),
  (8,'Richard', 'Sky st', 3,'richard@gmail',432567),
  (9,'Susan', 'One way', 9,'susan@gmail',456754),
  (10,'Vicky', 'Yellow Garden', 2,'vicky@gmail',234543),
  (11,'Ben', 'Park Lane', 38,'ben@gmail',345678),
  (12,'William', 'Central st', 9,'willain@gmail',12345),
  (13,'Chuck', 'Main Road', 9,'bhrrtg@gmail',123654),
  (14,'Viola', 'Sideway', 16,'viola@gmail',456342)
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

