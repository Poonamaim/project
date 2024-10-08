import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="NEELAM10$",
  database="mydb"
)

mycursor = mydb.cursor()

res = mycursor.execute("""
CREATE TABLE customer_poonam_ke (
personid int not null Auto_increment,
StudentName varchar(255) not null,
firstName   varchar(255),
age int,
email varchar(200),
mobile varchar(14),
primary key (personid)
)
""")
print(res)
