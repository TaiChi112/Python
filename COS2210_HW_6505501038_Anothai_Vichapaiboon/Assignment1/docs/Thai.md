[Back to English](../README.md)

# Assignment1 - การวิเคราะห์ข้อความแบบมัลติเธรด (ภาษาไทย)

### ภาพรวม
`Assignment1.py` เป็นสคริปต์ Python ที่ใช้มัลติเธรดในการวิเคราะห์ไฟล์ข้อความเพื่อ:
- ตรวจสอบคำหยาบ
- ตรวจสอบคำซ้ำในแต่ละบรรทัด
- ตรวจสอบบรรทัดที่มีจำนวนคำเกินกำหนด

### ข้อมูลนำเข้า
- **ไฟล์ข้อความ:** `badword.txt` ในโฟลเดอร์ `Assignment1/` (แต่ละบรรทัดจะถูกวิเคราะห์)
- **รายการคำหยาบ:** กำหนดไว้ในสคริปต์ (`fuck`, `bitch`, `cunt`, `damn`, `asshole`)
- **จำนวนคำสูงสุด:** ค่าเริ่มต้นคือ 12 คำต่อบรรทัด

### กระบวนการ
สคริปต์จะรัน 3 เธรดพร้อมกัน:
1. **ตรวจสอบคำหยาบ**
   - นับจำนวนคำหยาบแต่ละคำและบันทึกหมายเลขบรรทัดที่พบ
2. **ตรวจสอบคำซ้ำ**
   - หาบรรทัดที่มีคำซ้ำกัน
3. **ตรวจสอบบรรทัดที่เกินจำนวนคำ**
   - หาบรรทัดที่มีจำนวนคำมากกว่า 12 คำ

แต่ละเธรดจะแสดงผลลัพธ์ทางหน้าจอ

### ผลลัพธ์
- **ผลลัพธ์ที่แสดงทางหน้าจอ:**
  - จำนวนคำหยาบและหมายเลขบรรทัด
  - หมายเลขบรรทัดที่มีคำซ้ำ
  - หมายเลขบรรทัดที่เกินจำนวนคำที่กำหนด

### ตัวอย่างการใช้งาน
1. ใส่ข้อความใน `Assignment1/badword.txt`
2. รันสคริปต์:
   ```bash
   python Assignment1/Assignment1.py
   ```
3. ตัวอย่างผลลัพธ์:
   ```
   Thread1 Start working
   fuck: 2 คำ
   ...
   [2]
   Thread1 Finished working
   Thread2 Starts working
   [2, 4]
   Thread2 Finished working
   Thread3 Starts working
   [3]
   thread3 Finished working
   ```

### การปรับแต่ง
- เปลี่ยนคำหยาบ: แก้ไขตัวแปร `bads`
- เปลี่ยนจำนวนคำสูงสุด: แก้ไขตัวแปร `limit`
- เปลี่ยนไฟล์นำเข้า: แก้ไขตัวแปร `file`

---

## คำอธิบายโค้ดทีละขั้นตอน

ด้านล่างนี้เป็นคำอธิบายโค้ดหลักใน `Assignment1.py` อย่างละเอียด ว่าแต่ละคำสั่งทำอะไร ตรวจสอบเงื่อนไขอะไร และคืนค่าอะไร

### การนำเข้าโมดูล

```python
import threading
import time
```
**นำเข้าโมดูล threading (สำหรับรันแบบขนาน) และ time (สำหรับหน่วงเวลา)**

---

### ฟังก์ชัน: `duplicate(lst)`

```python
def duplicate(lst):
   for i in range(len(lst)):
      if lst[i] in lst[i+1:]:
         return True, lst[i]
   return False, None
```
- **หน้าที่:** ตรวจสอบว่ามีคำใดในลิสต์ซ้ำหรือไม่
- **วิธีการ:**
  - วนลูปแต่ละคำในลิสต์
  - สำหรับแต่ละคำ ตรวจสอบว่าคำนั้นมีอยู่ในส่วนที่เหลือของลิสต์หรือไม่ (`lst[i+1:]`)
- **เงื่อนไขที่ตรวจสอบ:** `if lst[i] in lst[i+1:]:` (คำนี้ซ้ำหรือไม่)
- **คืนค่า:**
  - ถ้าพบคำซ้ำ: คืนค่า `True` และคำนั้น
  - ถ้าไม่พบ: คืนค่า `False` และ `None`

---

### ฟังก์ชัน: `findBadword(file, bads)`

```python
def findBadword(file,bads):
   bad_pos = []
   count = 1
   try:
      print('Thread1 Start working')
      with open(file, 'r',encoding = 'utf-8') as fp:
         contents = fp.readlines()
         for line in contents:
            clean_line = []
            for w in line.strip().split():
               clean_line.append(w.strip('.?",\'').lower())
            for bad in bads:
               if bad in clean_line:
                  bads[bad] += clean_line.count(bad)
                  if count not in bad_pos:
                     bad_pos.append(count)
            count+=1
         for key, value in bads.items():
            print(f'{key}: {value} คำ')
         print(bad_pos)
         print('Thread1 Finished working')
   except Exception as e:
      print(e.__class__)
```
- **หน้าที่:** อ่านไฟล์ นับจำนวนคำหยาบแต่ละคำ และบันทึกหมายเลขบรรทัดที่พบคำหยาบ
- **วิธีการ:**
  - เปิดไฟล์และอ่านทุกบรรทัด
  - สำหรับแต่ละบรรทัด แยกและล้างคำ
  - สำหรับแต่ละคำหยาบ ตรวจสอบว่ามีในบรรทัดหรือไม่
  - **เงื่อนไขที่ตรวจสอบ:** `if bad in clean_line:` (มีคำหยาบในบรรทัดนี้หรือไม่)
  - ถ้าพบ เพิ่มจำนวนและบันทึกหมายเลขบรรทัด
  - แสดงผลลัพธ์
- **คืนค่า:** ไม่มี (แสดงผลทางหน้าจอ)

---

### ฟังก์ชัน: `findrepeat(file)`

```python
def findrepeat(file):
   repeat = []
   count = 1
   try:
      print('Thread2 Starts working')
      with open(file, 'r', encoding = 'utf-8') as fp:
         contents = fp.readlines()
         for line in contents:
            clean_line = []
            for w in line.strip().split():
               clean_line.append(w.strip('.?,"\'').lower())
            found,word = duplicate(clean_line)
            if found:
               repeat.append(count)
            count+=1
            time.sleep(0.04)
         print(repeat)
         print('Thread2 Finished working')
   except Exception as e:
      print(e.__class__)
```
- **หน้าที่:** หาบรรทัดที่มีคำซ้ำ
- **วิธีการ:**
  - เปิดไฟล์และอ่านทุกบรรทัด
  - สำหรับแต่ละบรรทัด แยกและล้างคำ
  - เรียกใช้ `duplicate(clean_line)` เพื่อตรวจสอบคำซ้ำ
  - **เงื่อนไขที่ตรวจสอบ:** `if found:` (มีคำซ้ำหรือไม่)
  - ถ้าพบ บันทึกหมายเลขบรรทัด
  - แสดงผลลัพธ์
- **คืนค่า:** ไม่มี (แสดงผลทางหน้าจอ)

---

### ฟังก์ชัน: `findOver(file, limit)`

```python
def findOver(file,limit):
   over = []
   count = 1
   try:
      print('Thread3 Starts working')
      with open(file, 'r', encoding = 'utf-8') as fp:
         contents = fp.readlines()
         for line in contents:
            clean_line = []
            for w in line.strip().split():
               clean_line.append(w.strip('.?",\'').lower())
            lens = len(clean_line)
            if limit < lens:
               over.append(count)
            count+=1
            time.sleep(0.08)
         print(over)
         print('thread3 Finished working')
   except Exception as e:
      print(e.__class__)
```
- **หน้าที่:** หาบรรทัดที่มีจำนวนคำมากกว่าที่กำหนด
- **วิธีการ:**
  - เปิดไฟล์และอ่านทุกบรรทัด
  - สำหรับแต่ละบรรทัด แยกและล้างคำ
  - นับจำนวนคำในบรรทัด
  - **เงื่อนไขที่ตรวจสอบ:** `if limit < lens:` (บรรทัดนี้ยาวเกินกำหนดหรือไม่)
  - ถ้าใช่ บันทึกหมายเลขบรรทัด
  - แสดงผลลัพธ์
- **คืนค่า:** ไม่มี (แสดงผลทางหน้าจอ)

---

### ส่วนหลักของโปรแกรม

```python
limit = 12
bads = {'fuck':0,'bitch':0,'cunt':0,'damn':0,'asshole':0}
file = './Assignment1/badword.txt'
thread1 = threading.Thread(target=findBadword,args=(file,bads))
thread2 = threading.Thread(target = findrepeat, args = (file,))
thread3 = threading.Thread(target=findOver,args=(file,limit))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
```
- **หน้าที่:** ตั้งค่าและรันฟังก์ชันวิเคราะห์ทั้งสามแบบขนานกัน
- **วิธีการ:**
  - กำหนดจำนวนคำสูงสุดและคำหยาบ
  - กำหนด path ของไฟล์
  - สร้าง thread สำหรับแต่ละฟังก์ชัน
  - สั่งให้ทุก thread เริ่มทำงาน (รันพร้อมกัน)
  - รอให้ทุก thread ทำงานเสร็จก่อนจบโปรแกรม

---

**สรุป:**
- แต่ละฟังก์ชันรับผิดชอบงานวิเคราะห์เฉพาะด้าน
- มีการตรวจสอบเงื่อนไขเพื่อหาคำหยาบ คำซ้ำ หรือบรรทัดที่เกินจำนวนคำ
- ผลลัพธ์แสดงทางหน้าจอ ไม่ได้คืนค่า
- ใช้มัลติเธรดเพื่อให้วิเคราะห์ได้พร้อมกัน
