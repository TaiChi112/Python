
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
    
    
def main():
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
    return 0

main()