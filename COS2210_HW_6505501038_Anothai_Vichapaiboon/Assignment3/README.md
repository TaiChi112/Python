[English](README.md) | [Thai](./docs/Thai.md)

## Step-by-Step Code Explanation

Below is a detailed explanation of the main code in `Assignment3.py`, describing what each statement does, what conditions are checked, and what is returned.

### Imports

```python
from pyzbar.pyzbar import decode
from PIL import Image
import os
import qrcode
import mysql.connector
from mysql.connector import Error
```
**Imports libraries for QR code processing, image handling, file operations, QR code generation, and MySQL database access.**

---

### Database Creation

```python
conn = mysql.connector.connect(...)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS Person")
```
- **What is this?** Connects to MySQL and creates a database if it doesn't exist.
- **What does it do?** Ensures the database is ready for use.
- **What does it return?** None (side effect: database created).

---

### Table Creation

```python
conn = mysql.connector.connect(..., database='Person')
cursor = conn.cursor()
cursor.execute("""
   CREATE TABLE IF NOT EXISTS Persons (...)
""")
conn.commit()
```
- **What is this?** Connects to the `Person` database and creates the `Persons` table if it doesn't exist.
- **What does it do?** Ensures the table is ready for data insertion.
- **What does it return?** None (side effect: table created).

---

### QR Code Reading

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
- **What is this?** Function to decode a QR code image and extract the embedded data.
- **What does it do?** Opens the image, decodes QR codes, and returns the first decoded string.
- **What does it return?** The decoded string from the QR code.

---

### Data Transformation

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
- **What is this?** Converts a list of string records into tuples with specified data types.
- **What does it do?** Splits each record and casts each field to the correct type.
- **What does it return?** A list of tuples ready for database insertion.

---

### QR Code Generation

```python
def generate_qr_code(data):
   qr = qrcode.QRCode(...)
   qr.add_data(data)
   qr.make(fit=True)
   img = qr.make_image(...)
   return img
```
- **What is this?** Function to generate a QR code image from a string.
- **What does it do?** Creates and returns a QR code image object.
- **What does it return?** The QR code image.

---

### Main Data Flow

- **Sample data is defined as a list of strings.**
- **QR codes are generated and saved as images.**
- **Images are read and decoded to extract data.**
- **Data is transformed and inserted into the database.**
- **SQL queries are run to filter and export data to text files.**

---

**Summary:**
- The script demonstrates QR code generation, decoding, data transformation, and MySQL integration.
- Each function is responsible for a specific task in the workflow.
- The output includes QR images, a populated database, and filtered text files.


<!-- # Assignment3 - QR Code Data Processing and MySQL Integration (English/Thai)

## English Version

### Overview
`Assignment3.py` is a Python script that demonstrates the integration of QR code generation/decoding, data transformation, and MySQL database operations. It generates QR codes from sample personal data, decodes them, stores the data in a MySQL database, and exports filtered results to text files.

### Inputs
- **Sample Data:** A list of 20 personal records (name, age, sex, occupation, salary, telephone, email) is hardcoded in the script.
- **QR Images:** QR codes are generated and saved in `Assignment3/qr_images/`.
- **Database:** MySQL server running on `localhost` (port 3307, user `root`, no password by default).
- **No user input is required.**

### Processes
1. **Database Setup:**
   - Connects to MySQL and creates a database `Person` and a table `Persons` if they do not exist.
2. **QR Code Generation:**
   - Generates QR codes for each sample record and saves them as images.
3. **QR Code Decoding:**
   - Reads and decodes all QR images in the folder, extracting the original data.
4. **Data Transformation:**
   - Splits and converts the decoded data into appropriate types for database insertion.
5. **Database Insertion:**
   - Inserts all records into the `Persons` table.
6. **Data Querying and Export:**
   - Queries for all records, males with salary > 20,000, and females aged ≤ 45.
   - Exports the filtered results to `Male_over20000.txt` and `Female_under45.txt`.

### Outputs
- **QR Code Images:**
  - 20 QR code images in `Assignment3/qr_images/`.
- **MySQL Database:**
  - Database `Person` with table `Persons` containing all records.
- **Text Files:**
  - `Assignment3/Male_over20000.txt`: Males with salary > 20,000
  - `Assignment3/Female_under45.txt`: Females aged ≤ 45
- **Console Output:**
  - Prints all records and filtered results.

### Example Usage
1. Install dependencies:
   ```bash
   pip install pyzbar pillow qrcode mysql-connector-python
   ```
   - You may need to install zbar for `pyzbar` to work (see pyzbar documentation).
2. Ensure MySQL is running on port 3307 with user `root` and no password.
3. Run the script:
   ```bash
   python Assignment3/Assignment3.py
   ```
4. Check the generated QR images and output text files in the `Assignment3/` folder.

### Customization
- Change sample data: Edit the `data` list in the script.
- Change MySQL connection: Edit the connection parameters.
- Change output file names or query conditions as needed. -->
