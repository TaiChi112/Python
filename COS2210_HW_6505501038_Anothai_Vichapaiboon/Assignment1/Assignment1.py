import threading
import time
def duplicate(lst):
    for i in range(len(lst)):
        if lst[i] in lst[i+1:]:
            return True, lst[i]
    return False, None

## Without list comprehension
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