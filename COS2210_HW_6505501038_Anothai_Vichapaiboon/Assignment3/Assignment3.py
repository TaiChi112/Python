
from pyzbar.pyzbar import decode
from PIL import Image
import os
import qrcode

import mysql.connector
from mysql.connector import Error




try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        port = '3307'
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS Person")
    print("Database created successfully.")
except Error as e:
    print("Error creating database", e)
else:
    cursor.close()
    conn.close()


conn = mysql.connector.connect(host='localhost', user='root',password='',port = '3307',database = 'Person')
cursor = conn.cursor()
query = """
    CREATE TABLE IF NOT EXISTS Persons (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        age INT,
        sex VARCHAR(1),
        occupation VARCHAR(50),
        salary DECIMAL(10, 2),
        telephone VARCHAR(15),
        email VARCHAR(255)
    );
    """
cursor.execute(query)
conn.commit()



def read_qr_code(image_path):
    image = Image.open(image_path)
    decoded_objects = decode(image)
    records = []
    for obj in decoded_objects:
        data = obj.data.decode('utf-8')
        records.append(data)
    return records[0]

def record_transform(contents, field_type):
    emp = []
    for rec in contents:
        x = rec.split()
        y = []
        for i in range(len(x)):
            y.append(field_type[i](x[i]))
        emp.append(tuple(y))
    return emp 

def process_images(path):
    files = os.listdir(path)
    records = []
    for fname in files:
        if fname.endswith(('.jpg', '.jpeg', '.png', '.bmp')):  
            filepath = os.path.join(path, fname)
            record = read_qr_code(filepath)
            records.append(record)
    return records


def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img



data = [
    "Kittipong 22 M Student 9500 0812345678 kittipong01@example.com",
    "Waraporn 27 F Accountant 12000 0898765432 waraporn02@example.com",
    "Supachai 30 M Engineer 18000 0823456789 supachai03@example.com",
    "Supawadee 19 F Student 5000 0845678910 supawadee04@example.com",
    "Nattawut 35 M Programmer 20000 0867890123 nattawut05@example.com",
    "Preeyanuch 28 F Designer 15000 0834567890 preeyanuch06@example.com",
    "Adisak 40 M Manager 30000 0810987654 adisak07@example.com",
    "Jaruwan 25 F Researcher 17000 0890123456 jaruwan08@example.com",
    "Peerapat 33 M Teacher 25000 0876543210 peerapat09@example.com",
    "Nipaporn 24 F Salesperson 14000 0865432109 nipaporn10@example.com",
    "Phattharaphon 29 M Analyst 22000 0822222222 phattharaphon11@example.com",
    "Nattha 32 F Police 19500 0855555555 nattha12@example.com",
    "Teeraphat 21 M Student 8000 0844444444 teeraphat13@example.com",
    "Pimchanok 26 F Translator 16000 0833333333 pimchanok14@example.com",
    "Wasun 45 M Entrepreneur 32000 0821111111 wasan15@example.com",
    "Orawan 31 F Reseacher 21000 0861234567 orawan16@example.com",
    "Phongsakorn 23 M Security 11000 0893216547 phongsakorn17@example.com",
    "Suchada 38 F Lawyer 28000 0884567890 suchada18@example.com",
    "Teerawat 65 M Consultant 35000 0810001111 teerawat19@example.com",
    "Chanakan 18 F Student 6000 0836547890 chanakan20@example.com"
]




count = 1
for dt in data :
    img = generate_qr_code(dt)
    img.save(f'./Assignment3/qr_images/image{count}.png')
    count+=1


image_folder = './Assignment3/qr_images'
records = process_images(image_folder)
print(records)


data_field = [str,int,str,str,float,str,str]
rec = record_transform(records,data_field)
print(rec)


query = """
    INSERT INTO persons (name, age, sex,occupation,salary,telephone,email)
    VALUES (%s, %s, %s, %s, %s ,%s, %s);
    """

cursor.executemany(query,rec)
conn.commit()


cursor.execute('SELECT * FROM Persons')
rows = cursor.fetchall()
for row in rows:
        print(row, type(row))


cursor.execute('SELECT * FROM Persons WHERE sex = "M" and salary> 20000')
rows = cursor.fetchall()
for row in rows:
        print(row, type(row))


text_list = []

for row in rows:
    text = ''
    for col in row:
        t = str(col)
        text+=t
        if col != row[-1]:
            text+=','    
    print(text)
    text_list.append(text)
print(text_list)

try:
    with open("./Assignment3/Male_over20000.txt", "w",  encoding="utf-8") as fp:
        fp.write('\n'.join(text_list))
except Exception as e:
    print(e.__class__,e.args[1])


cursor.execute('SELECT * FROM Persons WHERE sex = "F" and age <=45')
rows2 = cursor.fetchall()
for row in rows2:
        print(row, type(row))

text_list = []

for row in rows2:
    text = ''
    for col in row:
        t = str(col)
        text+=t
        if col != row[-1]:
            text+=','    
    print(text)
    text_list.append(text)
print(text_list)

try:
    with open("./Assignment3/Female_under45.txt", "w",  encoding="utf-8") as fp:
        fp.write('\n'.join(text_list))
except Exception as e:
    print(e.__class__,e.args[1])





