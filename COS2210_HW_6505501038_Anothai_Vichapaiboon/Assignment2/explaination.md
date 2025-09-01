# Assignment2.py Code Explanation

## ภาพรวมโปรแกรม
`Assignment2.py` เป็นโปรแกรมสำหรับ web scraping ข้อมูลจาก Wikipedia (เกี่ยวกับสถานีโทรทัศน์ไทยพีบีเอส) แล้วนำข้อมูลตารางที่ได้มาแปลงเป็นตารางในไฟล์ Word (.docx) โดยใช้ไลบรารี requests, BeautifulSoup, lxml และ python-docx

---

## Input ของโปรแกรม
- **เว็บไซต์ Wikipedia**: URL ที่ใช้ดึงข้อมูลคือ https://th.wikipedia.org/wiki/สถานีโทรทัศน์ไทยพีบีเอส
- **ไม่มี input จากผู้ใช้โดยตรง**

---

## ตัวแปรสำคัญที่สร้างขึ้น
- `WIKI_URL`: เก็บ URL ของ Wikipedia ที่ต้องการดึงข้อมูล
- `OUTPUT_DOC_PATH`: path สำหรับบันทึกไฟล์ Word ที่สร้างขึ้น
- `response`: เก็บผลลัพธ์การ request หน้าเว็บ (HTML)
- `soup`: เก็บ BeautifulSoup object สำหรับ parse HTML
- `director_table`, `news_table`: เก็บ tag ตารางที่ต้องการดึงข้อมูล (ผู้อำนวยการ/รายการข่าว)
- `director_heading`, `news_heading`: เก็บ tag heading ของแต่ละตาราง
- `director_columns`, `news_columns`: เก็บ tag หัวตาราง (th) ของแต่ละตาราง
- `director_rows`, `news_rows`: เก็บ tag แถวข้อมูล (tr) ของแต่ละตาราง
- `doc`: เก็บ Document object สำหรับสร้างไฟล์ Word

---

## อธิบายแต่ละฟังก์ชัน/Scope

### 1. add_table_to_doc(document, row_data, heading_tag, column_tags)
- **Input**:
    - `document`: Document object ของ python-docx
    - `row_data`: list ของ tag <tr> (แถวข้อมูล)
    - `heading_tag`: tag heading ของตาราง
    - `column_tags`: list ของ tag <th> (หัวตาราง)
- **Output**: ไม่มี (เพิ่มตารางลงใน document)
- **การทำงาน**:
    - เพิ่ม heading ให้กับตารางในไฟล์ Word
    - สร้างตารางใหม่ใน document โดยมี 2 คอลัมน์
    - ใส่ชื่อหัวตารางจาก column_tags
    - วนลูปแต่ละแถวข้อมูล (row_data) เพื่อดึงข้อมูลแต่ละ cell (td) และใส่ลงในตาราง
    - กรณี cell มีหลายบรรทัด จะรวมข้อความเป็นบรรทัดเดียว
    - ลบ tag <sup> ที่เป็นอ้างอิงท้ายบรรทัดออก
- **Method ที่ใช้**:
    - `document.add_heading()`: เพิ่มหัวข้อในไฟล์ Word
    - `document.add_table()`: สร้างตารางใหม่
    - `table.style`: กำหนด style ของตาราง
    - `row_tag.find_all('td')`: ดึง cell ข้อมูลแต่ละแถว
    - `cell.get_text(strip=True)`: ดึงข้อความจาก cell
    - `row_tag.find_all('sup')`: ลบ tag อ้างอิงท้ายบรรทัด

---

## อธิบายการทำงานหลัก (Main Workflow)
1. **Request หน้าเว็บ**
    - ใช้ `requests.get(WIKI_URL)` เพื่อดึง HTML ของหน้าเว็บ
2. **Parse HTML ด้วย BeautifulSoup**
    - สร้าง object `soup` เพื่อค้นหา tag ต่าง ๆ ใน HTML
3. **ค้นหาและแยกตารางที่ต้องการ**
    - ใช้ `soup.find()` เพื่อค้นหา tag ตาราง (table) และ heading (h2/h3) ที่ต้องการ
    - แยกหัวตาราง (th) และแถวข้อมูล (tr) ออกมา
4. **สร้างไฟล์ Word และเพิ่มตาราง**
    - สร้าง Document object
    - เรียกใช้ `add_table_to_doc()` เพื่อเพิ่มตารางผู้อำนวยการและตารางรายการข่าวลงในไฟล์ Word
5. **บันทึกไฟล์ Word**
    - ใช้ `doc.save(OUTPUT_DOC_PATH)` เพื่อบันทึกไฟล์

---

## อธิบาย Method/Library ที่ใช้
- **requests.get()**: ดึงข้อมูล HTML จากเว็บไซต์
- **BeautifulSoup()**: แปลง HTML เป็น object ที่ค้นหา tag ได้ง่าย
- **soup.find() / find_all()**: ค้นหา tag ที่ต้องการใน HTML
- **Document()**: สร้างไฟล์ Word ใหม่
- **add_heading() / add_table()**: เพิ่ม heading และตารางในไฟล์ Word
- **get_text(strip=True)**: ดึงข้อความจาก tag HTML
- **os**: ใช้สำหรับจัดการ path (แต่ในโค้ดนี้ไม่ได้ใช้จริง)

---

## สรุป
Assignment2.py เป็นโปรแกรม web scraping ที่ดึงข้อมูลตารางจาก Wikipedia แล้วนำข้อมูลมาแปลงเป็นตารางในไฟล์ Word โดยใช้ BeautifulSoup สำหรับ parse HTML และ python-docx สำหรับสร้างไฟล์ Word โดยมีการแยก scope การทำงานชัดเจนและใช้ method ที่เหมาะสมกับงานแต่ละประเภท
