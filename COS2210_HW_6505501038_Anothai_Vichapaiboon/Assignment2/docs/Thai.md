[Back to English](../README.md)

## คำอธิบายโค้ดทีละขั้นตอน

ด้านล่างนี้เป็นคำอธิบายโค้ดหลักใน `assignment2.py` อย่างละเอียด ว่าแต่ละคำสั่งทำอะไร ตรวจสอบเงื่อนไขอะไร และคืนค่าอะไร

### การนำเข้าโมดูล

```python
import requests
from bs4 import BeautifulSoup
import lxml
from docx import Document
import os
```
**นำเข้าไลบรารีที่จำเป็นสำหรับการดึงเว็บ, แยก HTML, สร้างเอกสาร และจัดการไฟล์**

---

### URL และการดึงเว็บ

```python
url = 'https://th.wikipedia.org/wiki/สถานีโทรทัศน์ไทยพีบีเอส'
response = requests.get(url)
```
- **คืออะไร:** กำหนด URL ของ Wikipedia และส่ง HTTP GET เพื่อดึงหน้าเว็บ
- **ทำอะไร:** ดาวน์โหลด HTML ของหน้าเว็บ
- **คืนค่า:** `response` คือผลลัพธ์ที่ได้จากเซิร์ฟเวอร์ (รวม HTML)

---

### การแยกวิเคราะห์ HTML

```python
soup = BeautifulSoup(response.text,'html.parser')
```
- **คืออะไร:** สร้างอ็อบเจ็กต์ BeautifulSoup เพื่อแยก HTML
- **ทำอะไร:** ใช้ค้นหาและดึง element ต่าง ๆ จาก HTML

---

### การดึงตาราง

```python
Reporter_table = soup.find('table',{'class':'toccolours'})
director_head = soup.find('h3',{'id':'ผู้อำนวยการสถานีฯ'})
columns = Reporter_table.findAll('th')
rows = Reporter_table.findAll('tr')
table_data = rows[2:]

Schedules_table = soup.find('table',{'class':'wikitable'})
head = Schedules_table.find_all('th')
tr = Schedules_table.find_all('tr')
table_data2 = tr[1:]
h2 = soup.find('h2',{'id':'รายการข่าวของสถานี_ฯ'})
```
- **คืออะไร:** ค้นหาตารางและหัวข้อที่เกี่ยวข้องใน HTML
- **ทำอะไร:**
  - `Reporter_table` คือตารางผู้อำนวยการ
  - `director_head` คือหัวข้อผู้อำนวยการ
  - `columns` และ `rows` คือหัวตารางและแถว
  - `table_data` ข้าม 2 แถวแรก (มักเป็นหัวตาราง)
  - `Schedules_table`, `head`, `tr`, `table_data2`, `h2` สำหรับตารางรายการข่าว

---

### การสร้างไฟล์ Word

```python
doc = Document()
```
- **คืออะไร:** สร้างอ็อบเจ็กต์เอกสาร Word ใหม่
- **ทำอะไร:** เตรียมเพิ่มเนื้อหาและตารางลงไฟล์ .docx

---

### ฟังก์ชัน: `docWrite(docs, tables, head, columns)`

```python
def docWrite(docs,tables,head,columns):
   docs.add_heading(head.get_text(strip=True),1)
   table = docs.add_table(rows=1,cols=2)
   table.style = 'Table Grid'
   header = table.rows[0].cells
   for i in range(len(header)):
      header[i].text = columns[i].get_text(strip = True)
   for data in tables:
      cells = data.find_all('td')
      row = table.add_row().cells
      for sup in data.find_all('sup'):
         sup.decompose()
      if len(cells) == 1:
         row[0].text = ""
         row[1].text = cells[0].get_text(strip=True)
      elif len(cells) == 2:
         row[0].text = cells[0].get_text(strip = True)
         text_list = [text.strip() for text in cells[1].stripped_strings]
         if len(text_list) == 1:
            row[1].text = cells[1].get_text(strip = True)
         else:
            content = " ".join(f'{line}' for line in text_list)
            row[1].text = content
```
- **คืออะไร:** ฟังก์ชันสำหรับเขียนตารางลงเอกสาร Word
- **ทำอะไร:**
  - เพิ่มหัวข้อในเอกสาร
  - สร้างตาราง 2 คอลัมน์
  - ใส่ชื่อหัวตาราง
  - สำหรับแต่ละแถวข้อมูล:
   - ลบเลขอ้างอิง (superscript)
   - จัดการแถวที่มี 1 หรือ 2 คอลัมน์
   - รวมเนื้อหาหลายบรรทัดถ้ามี
- **คืนค่า:** ไม่มี (แก้ไขเอกสารโดยตรง)

---

### การเขียนข้อมูลลงเอกสาร

```python
docWrite(doc,table_data,director_head,columns)
docWrite(doc,table_data2,h2,head)
```
- **คืออะไร:** เรียกฟังก์ชันเพื่อเพิ่มตารางทั้งสองลงเอกสาร
- **ทำอะไร:** เพิ่มตารางผู้อำนวยการและตารางรายการข่าวลงไฟล์ Word

---

### การบันทึกเอกสาร

```python
doc.save('./Assignment2/ThaiPBS_Webscrapping.docx')
```
- **คืออะไร:** บันทึกเอกสาร Word ไปยัง path ที่กำหนด
- **ทำอะไร:** เขียนเนื้อหาทั้งหมดลงไฟล์ .docx
- **คืนค่า:** ไม่มี (สร้าง/เขียนทับไฟล์)

---

**สรุป:**
- สคริปต์นี้ดึงและแยกข้อมูลจาก Wikipedia แล้วเขียนลงไฟล์ Word
- ทุกขั้นตอนหลักถูกจัดการโดยโค้ดหรือฟังก์ชันเฉพาะ
- ผลลัพธ์คือไฟล์ .docx ที่จัดรูปแบบพร้อมข้อมูลที่ดึงมา


<!-- [Back to English](../README.md)

### ภาพรวม
`assignment2.py` เป็นสคริปต์ Python สำหรับดึงข้อมูลจากหน้า Wikipedia ภาษาไทยเรื่อง "สถานีโทรทัศน์ไทยพีบีเอส" และบันทึกข้อมูลในรูปแบบเอกสาร Microsoft Word โดยจะดึงข้อมูลจาก 2 ตาราง ได้แก่ รายชื่อผู้อำนวยการสถานี และตารางรายการข่าว

### ข้อมูลนำเข้า
- **URL เป้าหมาย:**
  - https://th.wikipedia.org/wiki/สถานีโทรทัศน์ไทยพีบีเอส
- **ไม่ต้องกรอกข้อมูลใด ๆ เพิ่มเติม**
- **ไลบรารีที่ต้องใช้:**
  - `requests`, `beautifulsoup4`, `lxml`, `python-docx`, `os`

### กระบวนการ
1. **ดึงหน้าเว็บ:**
   - ดาวน์โหลด HTML ของหน้า Wikipedia ด้วย `requests`
2. **แยกวิเคราะห์ HTML:**
   - ใช้ BeautifulSoup เพื่อแยกโครงสร้าง HTML
   - ค้นหาตารางผู้อำนวยการสถานี (class `toccolours`)
   - ค้นหาตารางรายการข่าว (class `wikitable`)
3. **ดึงข้อมูล:**
   - ดึงหัวตารางและแถวข้อมูลจากทั้งสองตาราง
   - ลบเลขอ้างอิง (superscript)
4. **สร้างไฟล์ Word:**
   - สร้างเอกสาร Word ใหม่
   - เพิ่มหัวข้อและตารางสำหรับแต่ละส่วน
   - เติมข้อมูลลงในตาราง
5. **บันทึกไฟล์:**
   - บันทึกเป็น `Assignment2/ThaiPBS_Webscrapping.docx`

### ผลลัพธ์
- **ไฟล์ Microsoft Word:**
  - `Assignment2/ThaiPBS_Webscrapping.docx` ประกอบด้วย
    - ตารางผู้อำนวยการสถานี
    - ตารางรายการข่าว

### ตัวอย่างการใช้งาน
1. ติดตั้งไลบรารีที่จำเป็น:
   ```bash
   pip install requests beautifulsoup4 lxml python-docx
   ```
2. รันสคริปต์:
   ```bash
   python Assignment2/assignment2.py
   ```
3. เปิดไฟล์ Word ที่สร้างขึ้นที่ `Assignment2/ThaiPBS_Webscrapping.docx`

### การปรับแต่ง
- เปลี่ยน URL Wikipedia ได้โดยแก้ไขตัวแปร `url`
- เปลี่ยนตำแหน่งไฟล์ผลลัพธ์ได้โดยแก้ไข `doc.save()` -->
