import mysql.connector  as mysql


conn= mysql.connect(
    host="localhost",
    password="",
    user="root",
    database="TesttingDataBase2"
)


mydb=conn.cursor()
# mydb.execute("CREATE TABLE usamna (name VARCHAR(225) , address VARCHAR(225))")


#  Checking the available tables 
mydb.execute("SHOW TABLES")
for db in mydb:
    print(db)

# mydbb=conn.cursor()
# mydbb.execute(" ")
