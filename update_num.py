

import pymysql

connection=pymysql.connect(
                host='localhost',
                user='root',
                password='6666',
                database='PhoneBook'
        )

cursor=connection.cursor()

name=input("Enter name to update: " )
field=input ("field to update: ")
value=input("\nupdate value: ")

#SQLQuery="UPDATE phone_book SET {}=? WHERE first_name LIKE ?".format(field)
SQLQuery=f"UPDATE phone_book SET {field} = '{value}' WHERE first_name LIKE '{name}'"

if cursor.execute(SQLQuery):
    connection.commit()
    print("success")

else:
    print ("An Unknown Error Occured")

cursor.close()
connection.close()
