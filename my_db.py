
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",               #hostname
  user="root",                   # the user who has privilege to the db
  passwd="jay@9352*Mysql",               #password for user
    auth_plugin = 'mysql_native_password',

)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)
