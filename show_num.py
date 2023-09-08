import pymysql


connection=pymysql.connect(
            host="localhost",
            database="PhoneBook",
            user="root",
            password="6666"
        )

cursor=connection.cursor()

name=input("Enter Name to Check: ")

sql_query=f"SELECT * FROM phone_book WHERE first_name LIKE '{name}'"
#results=cursor.fetchall()


if cursor.execute(sql_query):
    results=cursor.fetchall()
    for item in results:
        print (item)
    connection.commit()
    print("success")

else:
    print ("An Error Occurred")

cursor.close()
connection.close()
