# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))






# import datetime

# x = datetime.datetime.now()
# print(x)

# try:
#     print(x)

# try:
#     print(x)
# except:
#     print("X not Define ")


import mysql.connector as myql
database='TesttingDataBase2'
con=myql.connect( host="localhost" , password="" , user="root" )

if not con:
      print(' Connection has not been established successfully !')
else:
      # Sleep(12)
      console_databases=[]
      mycursor=con.cursor()
      # mycursor.execute(f'CREATE DATABASE {database}')
      mycursor.execute("SHOW DATABASES")
      print(' Databse are :')
      for databses in mycursor:
            test=list(databses)
            console_databases.append(test)
      #  showing all the Databases
      # print(console_databases)

      # # print(f'All Data Bases are {console_databases}') 


      # for i in console_databases:
      #             print(i[0].upper())
            
                  
            









# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd=""
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE myNewDataBAse")