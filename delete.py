#Delete Entry

import pymysql

connection=pymysql.connect(
        host='localhost',
        password='6666',
        database='PhoneBook',
        user='root')

dlt=input("Enter Name to Delete: ")
cursor=connection.cursor()
SQLQuery=f"DELETE FROM phone_book WHERE first_name LIKE '{dlt}'"



if cursor.execute(SQLQuery):
    connection.commit()
    print (f"{dlt} deleted!")
    
else:
    print("Failed!")

cursor.close()
connection.close()
