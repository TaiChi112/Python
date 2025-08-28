[Back to English](../README.md)

## คำอธิบายโค้ดทีละขั้นตอน

ด้านล่างนี้เป็นคำอธิบายโค้ดหลักใน `Assignment3.py` อย่างละเอียด ว่าแต่ละคำสั่งทำอะไร ตรวจสอบเงื่อนไขอะไร และคืนค่าอะไร

### การนำเข้าโมดูล

```python
from pyzbar.pyzbar import decode
from PIL import Image
import os
import qrcode
import mysql.connector
from mysql.connector import Error
```
**นำเข้าไลบรารีสำหรับการประมวลผล QR code, จัดการภาพ, จัดการไฟล์, สร้าง QR code และเชื่อมต่อฐานข้อมูล MySQL**

---

### การสร้างฐานข้อมูล

```python
conn = mysql.connector.connect(...)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS Person")
```
- **คืออะไร:** เชื่อมต่อ MySQL และสร้างฐานข้อมูลหากยังไม่มี
- **ทำอะไร:** เตรียมฐานข้อมูลให้พร้อมใช้งาน
- **คืนค่า:** ไม่มี (ผลข้างเคียง: สร้างฐานข้อมูล)

---

### การสร้างตาราง

```python
conn = mysql.connector.connect(..., database='Person')
cursor = conn.cursor()
cursor.execute("""
   CREATE TABLE IF NOT EXISTS Persons (...)
""")
conn.commit()
```
- **คืออะไร:** เชื่อมต่อฐานข้อมูล `Person` และสร้างตาราง `Persons` หากยังไม่มี
- **ทำอะไร:** เตรียมตารางให้พร้อมสำหรับการเพิ่มข้อมูล
- **คืนค่า:** ไม่มี (ผลข้างเคียง: สร้างตาราง)

---

### การอ่าน QR Code

```python
def read_qr_code(image_path):
   image = Image.open(image_path)
   decoded_objects = decode(image)
   records = []
   for obj in decoded_objects:
      data = obj.data.decode('utf-8')
      records.append(data)
   return records[0]
```
- **คืออะไร:** ฟังก์ชันสำหรับถอดรหัส QR code จากภาพและดึงข้อมูลที่ฝังอยู่
- **ทำอะไร:** เปิดภาพ, ถอดรหัส QR code, คืนค่าข้อมูลที่ถอดรหัสได้ตัวแรก
- **คืนค่า:** สตริงที่ถอดรหัสจาก QR code

---

### การแปลงข้อมูล

```python
def record_transform(contents, field_type):
   emp = []
   for rec in contents:
      x = rec.split()
      y = []
      for i in range(len(x)):
         y.append(field_type[i](x[i]))
      emp.append(tuple(y))
   return emp
```
- **คืออะไร:** แปลงลิสต์ของสตริงเป็นทูเพิลที่มีชนิดข้อมูลตามที่กำหนด
- **ทำอะไร:** แยกแต่ละฟิลด์และแปลงชนิดข้อมูลให้ถูกต้อง
- **คืนค่า:** ลิสต์ของทูเพิลที่พร้อมสำหรับเพิ่มลงฐานข้อมูล

---

### การสร้าง QR Code

```python
def generate_qr_code(data):
   qr = qrcode.QRCode(...)
   qr.add_data(data)
   qr.make(fit=True)
   img = qr.make_image(...)
   return img
```
- **คืออะไร:** ฟังก์ชันสำหรับสร้างภาพ QR code จากสตริง
- **ทำอะไร:** สร้างและคืนค่าอ็อบเจ็กต์ภาพ QR code
- **คืนค่า:** ภาพ QR code

---

### ลำดับการทำงานหลัก

- **ข้อมูลตัวอย่างถูกกำหนดเป็นลิสต์ของสตริง**
- **สร้าง QR code และบันทึกเป็นภาพ**
- **อ่านและถอดรหัสภาพเพื่อดึงข้อมูล**
- **แปลงข้อมูลและเพิ่มลงฐานข้อมูล**
- **รัน SQL query เพื่อกรองและส่งออกข้อมูลเป็นไฟล์ข้อความ**

---

**สรุป:**
- สคริปต์นี้สาธิตการสร้าง/อ่าน QR code, แปลงข้อมูล, และเชื่อมต่อ MySQL
- แต่ละฟังก์ชันรับผิดชอบงานเฉพาะใน workflow
- ผลลัพธ์คือ QR images, ฐานข้อมูลที่มีข้อมูล และไฟล์ข้อความที่กรองแล้ว
## ภาษาไทย (Thai Version)

### ภาพรวม
`Assignment3.py` เป็นสคริปต์ Python ที่สาธิตการสร้างและอ่าน QR code, แปลงข้อมูล, และเชื่อมต่อกับฐานข้อมูล MySQL โดยจะสร้าง QR code จากข้อมูลตัวอย่าง, ถอดรหัส, บันทึกลงฐานข้อมูล และส่งออกผลลัพธ์ที่กรองแล้วเป็นไฟล์ข้อความ

### ข้อมูลนำเข้า
- **ข้อมูลตัวอย่าง:** ข้อมูลบุคคล 20 รายการ (ชื่อ, อายุ, เพศ, อาชีพ, เงินเดือน, โทรศัพท์, อีเมล) กำหนดไว้ในสคริปต์
- **QR Images:** QR code จะถูกสร้างและบันทึกใน `Assignment3/qr_images/`
- **ฐานข้อมูล:** MySQL ที่รันบน `localhost` (port 3307, user `root`, ไม่มีรหัสผ่าน)
- **ไม่ต้องกรอกข้อมูลใด ๆ เพิ่มเติม**

### กระบวนการ
1. **ตั้งค่าฐานข้อมูล:**
   - เชื่อมต่อ MySQL สร้าง database `Person` และ table `Persons` หากยังไม่มี
2. **สร้าง QR Code:**
   - สร้าง QR code สำหรับแต่ละข้อมูลและบันทึกเป็นภาพ
3. **ถอดรหัส QR Code:**
   - อ่านและถอดรหัส QR code ทั้งหมดในโฟลเดอร์
4. **แปลงข้อมูล:**
   - แยกและแปลงข้อมูลเป็นชนิดที่เหมาะสมสำหรับฐานข้อมูล
5. **บันทึกลงฐานข้อมูล:**
   - เพิ่มข้อมูลทั้งหมดลงใน table `Persons`
6. **คิวรีและส่งออกข้อมูล:**
   - คิวรีข้อมูลทั้งหมด, ผู้ชายที่เงินเดือน > 20,000, และผู้หญิงอายุ ≤ 45
   - ส่งออกผลลัพธ์เป็นไฟล์ `Male_over20000.txt` และ `Female_under45.txt`

### ผลลัพธ์
- **QR Code Images:**
  - 20 ภาพ QR code ใน `Assignment3/qr_images/`
- **ฐานข้อมูล MySQL:**
  - Database `Person` และ table `Persons` ที่มีข้อมูลทั้งหมด
- **ไฟล์ข้อความ:**
  - `Assignment3/Male_over20000.txt`: ผู้ชายเงินเดือนมากกว่า 20,000
  - `Assignment3/Female_under45.txt`: ผู้หญิงอายุไม่เกิน 45
- **ผลลัพธ์หน้าจอ:**
  - แสดงข้อมูลทั้งหมดและผลลัพธ์ที่กรองแล้ว

### ตัวอย่างการใช้งาน
1. ติดตั้งไลบรารีที่จำเป็น:
   ```bash
   pip install pyzbar pillow qrcode mysql-connector-python
   ```
   - อาจต้องติดตั้ง zbar เพิ่มเติม (ดูเอกสาร pyzbar)
2. ตรวจสอบว่า MySQL รันอยู่ที่ port 3307 user `root` ไม่มีรหัสผ่าน
3. รันสคริปต์:
   ```bash
   python Assignment3/Assignment3.py
   ```
4. ตรวจสอบ QR images และไฟล์ผลลัพธ์ในโฟลเดอร์ `Assignment3/`

### การปรับแต่ง
- เปลี่ยนข้อมูลตัวอย่าง: แก้ไขตัวแปร `data`
- เปลี่ยนการเชื่อมต่อ MySQL: แก้ไขพารามิเตอร์การเชื่อมต่อ
- เปลี่ยนชื่อไฟล์ผลลัพธ์หรือเงื่อนไขคิวรีได้ตามต้องการ
