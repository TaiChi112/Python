import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='TaiChi',
    database='django_python'
)

cursor = connection.cursor()
cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

cursor.close()
connection.close()
