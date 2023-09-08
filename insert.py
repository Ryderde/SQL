import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='6666',
    database='PhoneBook'
)

print("Add a Number to The PhoneBook\n\n")
first_name = input("Enter New First Name: ")
last_name = input("Enter New Last Name: ")
number = input("Enter Phone Number: ")
address = input("Enter Address: ")

cursor = connection.cursor()
sql_query2 = "INSERT INTO phone_book (first_name, last_name, number, address) VALUES ('" + first_name + "', '" + last_name + "', '" + number + "', '" + address + "')"
cursor.execute("SELECT * FROM phone_book")
result = cursor.fetchall()

name_exists = False

for row in result:
    if first_name in row:
        name_exists = True
        break

if name_exists:
    print("Name already exists")
else:
    cursor.execute(sql_query2)
    connection.commit()
    print("New entry added to the PhoneBook")

cursor.close()
connection.close()

