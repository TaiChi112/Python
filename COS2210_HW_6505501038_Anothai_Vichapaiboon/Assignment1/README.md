[English](README.md) | [Thai](./Docs/Thai.md)

# Assignment1 - Multithreaded Text Analysis (English/Thai)

### Overview
`Assignment1.py` is a Python script that uses multithreading to analyze a text file for:
- Bad word occurrences
- Repeated words in a line
- Lines exceeding a word count limit

### Inputs
- **Text File:** `badword.txt` in the `Assignment1/` folder. Each line is analyzed.
- **Bad Words List:** Predefined in the script (`fuck`, `bitch`, `cunt`, `damn`, `asshole`).
- **Word Limit:** Default is 12 words per line.

### Processes
The script runs three threads in parallel:
1. **Bad Word Detection**
   - Counts each bad word and records line numbers where they appear.
2. **Repeated Word Detection**
   - Finds lines with any repeated word.
3. **Over Limit Detection**
   - Finds lines with more than 12 words.

Each thread prints its results to the console.

### Outputs
- **Console Output:**
  - Bad word counts and line numbers
  - Line numbers with repeated words
  - Line numbers exceeding the word limit

### Example Usage
1. Place your text in `Assignment1/badword.txt`.
2. Run the script:
   ```bash
   python Assignment1/Assignment1.py
   ```
3. Example output:
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

### Customization

Change bad words: Edit the `bads` dictionary.
Change word limit: Edit the `limit` variable.
Change input file: Edit the `file` variable.

---

## Step-by-Step Code Explanation

Below is a detailed explanation of the main code in `Assignment1.py`, describing what each statement does, what conditions are checked, and what is returned.

### Imports

```python
import threading
import time
```
**Imports the threading module (for parallel execution) and time module (for delays).**

---

### Function: `duplicate(lst)`

```python
def duplicate(lst):
   for i in range(len(lst)):
      if lst[i] in lst[i+1:]:
         return True, lst[i]
   return False, None
```
- **Purpose:** Checks if any word in the list appears more than once.
- **How:**
  - Loops through each element in the list.
  - For each element, checks if it appears again later in the list (`lst[i+1:]`).
- **Condition checked:** `if lst[i] in lst[i+1:]:` (Is the current word repeated later?)
- **Return:**
  - If a duplicate is found: `True` and the duplicated word.
  - If no duplicates: `False` and `None`.

---

### Function: `findBadword(file, bads)`

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
- **Purpose:** Reads the file, counts each bad word, and records line numbers where bad words appear.
- **How:**
  - Opens the file and reads all lines.
  - For each line, splits and cleans words.
  - For each bad word, checks if it is present in the line.
  - **Condition checked:** `if bad in clean_line:` (Is the bad word in this line?)
  - If found, increases the count and records the line number.
  - Prints the results.
- **Return:** None (prints to console).

---

### Function: `findrepeat(file)`

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
- **Purpose:** Finds which lines have repeated words.
- **How:**
  - Opens the file and reads all lines.
  - For each line, splits and cleans words.
  - Calls `duplicate(clean_line)` to check for repeated words.
  - **Condition checked:** `if found:` (Is there a repeated word?)
  - If found, records the line number.
  - Prints the results.
- **Return:** None (prints to console).

---

### Function: `findOver(file, limit)`

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
- **Purpose:** Finds lines with more words than the specified limit.
- **How:**
  - Opens the file and reads all lines.
  - For each line, splits and cleans words.
  - Counts the number of words.
  - **Condition checked:** `if limit < lens:` (Is the line longer than the limit?)
  - If so, records the line number.
  - Prints the results.
- **Return:** None (prints to console).

---

### Main Program

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
- **Purpose:** Sets up and runs all three analysis functions in parallel threads.
- **How:**
  - Sets the word limit and bad words.
  - Sets the file path.
  - Creates three threads, each for a different function.
  - Starts all threads (they run at the same time).
  - Waits for all threads to finish before ending the program.

---

**Summary:**
- Each function is responsible for a specific analysis task.
- Conditions are checked to find bad words, repeated words, or lines over the word limit.
- Results are printed to the console, not returned.
- Multithreading is used to run all analyses at the same time.

