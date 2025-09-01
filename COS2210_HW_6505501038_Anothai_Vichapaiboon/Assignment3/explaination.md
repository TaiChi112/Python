# Assignment3.py Code Explanation

## Overview
`Assignment3.py` เป็นโปรแกรมที่เกี่ยวข้องกับการสร้าง QR Code จากข้อมูลบุคคล, การอ่าน QR Code, การบันทึกและดึงข้อมูลจากฐานข้อมูล MySQL, และการส่งออกข้อมูลไปยังไฟล์ .txt ตามเงื่อนไขที่กำหนด

---

## Input ของโปรแกรม
- **ข้อมูลบุคคล** (sample_data/data): เป็นข้อมูล string ของแต่ละบุคคล เช่น ชื่อ อายุ เพศ อาชีพ เงินเดือน เบอร์โทร อีเมล
- **ไฟล์รูปภาพ QR Code**: ที่ถูกสร้างและเก็บไว้ในโฟลเดอร์ `qr_images`
- **ฐานข้อมูล MySQL**: ใช้สำหรับเก็บข้อมูลบุคคล

---

## ตัวแปรสำคัญที่สร้างขึ้น
- `DB_CONFIG`: dictionary สำหรับเก็บค่าการเชื่อมต่อฐานข้อมูล
- `QR_IMAGE_DIR`, `MALE_OUTPUT_PATH`, `FEMALE_OUTPUT_PATH`: path สำหรับเก็บไฟล์รูป QR และไฟล์ .txt
- `sample_data` หรือ `data`: list ของ string ข้อมูลบุคคล
- `field_types` หรือ `data_field`: list ของชนิดข้อมูลแต่ละฟิลด์ (str, int, float, ...)
- `person_records` หรือ `rec`: list ของ tuple ข้อมูลบุคคลที่แปลงชนิดข้อมูลแล้ว
- `decoded_records` หรือ `records`: list ของ string ที่ได้จากการ decode QR
- `male_rows`, `female_rows`, `rows`, `rows2`: ผลลัพธ์จากการ query ข้อมูลจากฐานข้อมูล
- `text_list`: list ของ string สำหรับเตรียมข้อมูลไปเขียนไฟล์ .txt

---

## อธิบายแต่ละฟังก์ชัน/Scope

### 1. ฟังก์ชันเกี่ยวกับ Database
- **create_database()**: สร้างฐานข้อมูลชื่อ Person ถ้ายังไม่มี
- **create_table()**: สร้างตาราง Persons ในฐานข้อมูล
- **insert_persons(records)**: เพิ่มข้อมูลบุคคลลงในตาราง Persons
- **fetch_persons(query)**: ดึงข้อมูลจากฐานข้อมูลตาม query ที่กำหนด

### 2. ฟังก์ชันเกี่ยวกับ QR Code
- **generate_qr_code(data_str/data)**: สร้าง QR Code จาก string ที่รับเข้ามา (ใช้ qrcode.QRCode)
- **save_qr_codes(data_list, output_dir)**: สร้างและบันทึก QR Code สำหรับแต่ละข้อมูลใน data_list
- **decode_qr_image(image_path)/read_qr_code(image_path)**: อ่าน QR Code จากไฟล์รูปภาพและคืนค่า string ข้อมูล
- **decode_all_qr_images(image_dir)/process_images(path)**: อ่าน QR Code จากไฟล์ทั้งหมดในโฟลเดอร์และคืนค่า list ของ string

### 3. ฟังก์ชันเกี่ยวกับการแปลงข้อมูล
- **transform_records(record_list, field_types)/record_transform(contents, field_type)**: แปลงข้อมูล string เป็น tuple โดยแปลงชนิดข้อมูลแต่ละฟิลด์ให้ถูกต้อง

### 4. ฟังก์ชันเกี่ยวกับการ export ข้อมูล
- **export_to_txt(rows, output_path)**: แปลงข้อมูลแต่ละ row เป็น string แล้วเขียนลงไฟล์ .txt

---

## อธิบายการทำงานในแต่ละขั้นตอน (Main Workflow)
1. **สร้างฐานข้อมูลและตาราง**
    - เรียกใช้ `create_database()` และ `create_table()`
2. **สร้าง QR Code และบันทึกไฟล์**
    - วนลูปข้อมูลใน `sample_data`/`data` แล้วใช้ `generate_qr_code()` สร้าง QR Code
    - บันทึกไฟล์ QR Code ลงในโฟลเดอร์ `qr_images`
3. **อ่าน QR Code จากไฟล์**
    - ใช้ `decode_all_qr_images()` หรือ `process_images()` เพื่ออ่านข้อมูลจาก QR Code ทุกไฟล์ในโฟลเดอร์
4. **แปลงข้อมูลเป็น tuple**
    - ใช้ `transform_records()` หรือ `record_transform()` เพื่อแปลงข้อมูล string เป็น tuple ตามชนิดข้อมูล
5. **บันทึกข้อมูลลงฐานข้อมูล**
    - ใช้ `insert_persons()` หรือ query insert เพื่อเพิ่มข้อมูลลงตาราง Persons
6. **Query ข้อมูลตามเงื่อนไข**
    - Query เพศชายที่เงินเดือนมากกว่า 20000 และเพศหญิงที่อายุน้อยกว่าหรือเท่ากับ 45
7. **Export ข้อมูลไปยังไฟล์ .txt**
    - ใช้ `export_to_txt()` หรือวนลูปแปลงข้อมูลเป็น string แล้วเขียนไฟล์ .txt

---

## อธิบาย Method/Library ที่ใช้
- **qrcode.QRCode**: สร้าง QR Code จากข้อมูล string
- **pyzbar.pyzbar.decode**: อ่าน/ถอดรหัส QR Code จากรูปภาพ
- **PIL.Image.open**: เปิดไฟล์รูปภาพ
- **os.makedirs / os.listdir / os.path.join**: จัดการไฟล์และโฟลเดอร์
- **mysql.connector.connect**: เชื่อมต่อฐานข้อมูล MySQL
- **cursor.execute / cursor.executemany**: สั่งงาน SQL กับฐานข้อมูล
- **with open(..., 'w', encoding='utf-8')**: เขียนไฟล์ข้อความ

---

## สรุป
Assignment3.py เป็นโปรแกรมที่นำข้อมูลบุคคลมาสร้าง QR Code, อ่าน QR Code กลับมาเป็นข้อมูล, บันทึกข้อมูลลงฐานข้อมูล MySQL และดึงข้อมูลตามเงื่อนไขไปเขียนไฟล์ .txt โดยใช้ฟังก์ชันและไลบรารีที่เกี่ยวข้องกับ QR, ฐานข้อมูล, และการจัดการไฟล์อย่างเป็นระบบและมีการแยก scope การทำงานชัดเจน
