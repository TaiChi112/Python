
class Node[T]:
    data:T
    nextNode:Node[T]

class Student:
    id:int
    name: str
    def __init__(self,id:int,name:str):
        self.id = id
        self.name = name

    # def display(self):
    #     print("My id is :",self.getId(), "& My name's :",self.getName())  
    
    # def getId(self):
    #     return self.id

    # def getName(self):
    #     return self.name

Human = {
    "id":112,
    "name":"TaiChi"
}
def add(a:int,b:int):
    return a+b
def sub(a:int,b:int):
    return a-b
def main():
    # Node1:Node[int] = Node[int]()
    # Node1.data = 112
    
    print(add(1,2))
    print(sub(1,2))
    Human["name"] = "Alice"
    print(Human["name"])
    # name = "TaiChi"
    # age = 112
    # print("My name is :",name, "& my age : ",age)
    id:int = 112
    name:str = "TaiChi"
    print(Student(id,name).__dict__)
    # Student(id,name).display()
    
    # Student(113,"Alice").display()
    # print(Student(113,"Alice").display())
    # Student(114,"Charlie").display()
    # Student(114,"Charlie").getId()
    # Student(114,"Charlie").getName()
    
    student1 = ["Alice","Bob","Charlie"]
    print(student1)

    return 0

main()