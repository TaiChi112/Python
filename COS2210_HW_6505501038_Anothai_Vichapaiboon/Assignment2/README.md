[English](README.md) | [Thai](./Docs/Thai.md)

## Step-by-Step Code Explanation

Below is a detailed explanation of the main code in `assignment2.py`, describing what each statement does, what conditions are checked, and what is returned.

### Imports

```python
import requests
from bs4 import BeautifulSoup
import lxml
from docx import Document
import os
```
**Imports the required libraries for web requests, HTML parsing, document creation, and file operations.**

---

### URL and Web Request

```python
url = 'https://th.wikipedia.org/wiki/สถานีโทรทัศน์ไทยพีบีเอส'
response = requests.get(url)
```
- **What is this?** Sets the target Wikipedia URL and sends an HTTP GET request to fetch the page.
- **What does it do?** Downloads the HTML content of the page.
- **What does it return?** `response` contains the server's response, including the HTML.

---

### HTML Parsing

```python
soup = BeautifulSoup(response.text,'html.parser')
```
- **What is this?** Creates a BeautifulSoup object to parse the HTML.
- **What does it do?** Allows searching and extracting elements from the HTML document.

---

### Table Extraction

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
- **What is this?** Finds the relevant tables and headers in the HTML.
- **What does it do?**
  - `Reporter_table` locates the directors table.
  - `director_head` finds the heading for directors.
  - `columns` and `rows` extract table headers and rows.
  - `table_data` skips the first two rows (usually headers).
  - `Schedules_table`, `head`, `tr`, `table_data2`, and `h2` do the same for the news schedule table.

---

### Word Document Creation

```python
doc = Document()
```
- **What is this?** Creates a new Word document object.
- **What does it do?** Prepares to add content and tables to a .docx file.

---

### Function: `docWrite(docs, tables, head, columns)`

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
- **What is this?** Defines a function to write a table to the Word document.
- **What does it do?**
  - Adds a heading to the document.
  - Creates a table with 2 columns.
  - Fills the header row with column names.
  - For each data row:
   - Removes superscript references.
   - Handles rows with 1 or 2 columns.
   - Joins multi-line content if needed.
- **What does it return?** Nothing (modifies the document in place).

---

### Writing Data to Document

```python
docWrite(doc,table_data,director_head,columns)
docWrite(doc,table_data2,h2,head)
```
- **What is this?** Calls the function to add both tables to the document.
- **What does it do?** Adds the directors and news schedule tables to the Word file.

---

### Saving the Document

```python
doc.save('./Assignment2/ThaiPBS_Webscrapping.docx')
```
- **What is this?** Saves the Word document to the specified path.
- **What does it do?** Writes all content to a .docx file.
- **What does it return?** None (creates/overwrites the file).

---

**Summary:**
- The script fetches and parses a Wikipedia page, extracts two tables, and writes them to a Word document.
- All major steps are handled by dedicated code blocks or functions.
- The output is a formatted .docx file with the extracted data.


<!-- [English](README.md) | [Thai](./Docs/Thai.md)

# Assignment2 - ThaiPBS Wikipedia Web Scraping (English/Thai)

### Overview
`assignment2.py` is a Python script that scrapes data from the Thai Wikipedia page for "สถานีโทรทัศน์ไทยพีบีเอส" (Thai PBS TV Station) and exports the information into a formatted Microsoft Word document. It extracts two tables: the list of station directors and the news program schedule.

### Inputs
- **Target URL:** The script fetches data from:
  - https://th.wikipedia.org/wiki/สถานีโทรทัศน์ไทยพีบีเอส
- **No user input is required.**
- **Dependencies:**
  - `requests`, `beautifulsoup4`, `lxml`, `python-docx`, `os`

### Processes
1. **Web Request:**
   - Downloads the HTML content of the Wikipedia page using `requests`.
2. **HTML Parsing:**
   - Parses the HTML with BeautifulSoup.
   - Locates the table of station directors (class `toccolours`).
   - Locates the table of news programs (class `wikitable`).
3. **Data Extraction:**
   - Extracts table headers and rows for both tables.
   - Cleans up superscript references (e.g., citation numbers).
4. **Word Document Generation:**
   - Creates a new Word document.
   - Adds headings and tables for each section.
   - Fills tables with the extracted data.
5. **File Output:**
   - Saves the document as `Assignment2/ThaiPBS_Webscrapping.docx`.

### Outputs
- **Microsoft Word Document:**
  - `Assignment2/ThaiPBS_Webscrapping.docx` containing:
    - A table of station directors
    - A table of news programs

### Example Usage
1. Ensure all dependencies are installed:
   ```bash
   pip install requests beautifulsoup4 lxml python-docx
   ```
2. Run the script:
   ```bash
   python Assignment2/assignment2.py
   ```
3. Open the generated Word file at `Assignment2/ThaiPBS_Webscrapping.docx`.

### Customization
- Change the target Wikipedia URL by editing the `url` variable.
- Adjust the output file path by changing the `doc.save()` argument.

---
 -->
