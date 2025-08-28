import requests
from bs4 import BeautifulSoup
import lxml
from docx import Document
import os

url = 'https://th.wikipedia.org/wiki/%E0%B8%AA%E0%B8%96%E0%B8%B2%E0%B8%99%E0%B8%B5%E0%B9%82%E0%B8%97%E0%B8%A3%E0%B8%97%E0%B8%B1%E0%B8%A8%E0%B8%99%E0%B9%8C%E0%B9%84%E0%B8%97%E0%B8%A2%E0%B8%9E%E0%B8%B5%E0%B8%9A%E0%B8%B5%E0%B9%80%E0%B8%AD%E0%B8%AA'


response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

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

doc = Document()

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
    

docWrite(doc,table_data,director_head,columns)
docWrite(doc,table_data2,h2,head)
doc.save('./Assignment2/ThaiPBS_Webscrapping.docx')





