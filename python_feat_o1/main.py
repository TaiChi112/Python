import class1
x0 = "awesome"
def myfunc():
    print("Python is " + x0)
    x = "fantastic"
def main()->int:
    print(class1.greet1("John"))
    class1.greet2("John")
    
    myfunc()
    
    x = 112
    print("x:",x)
    x, y,z = "Hello", "World", "Python"
    print("x:",x)
    print(type(x))
    print("y:",y)
    print("z:",z)
    
    name1= name2=name3 = "TaiChi"
    print("name:",name1)
    print("name:",name2)
    print("name:",name3)
    
    fruits = ["apple", "banana", "cherry"]
    x, y, z = fruits
    print("x:",x)
    print("y:",y)
    print("z:",z)
    
    x = 5
    y = 3
    print("result:",x+y)
    x = 1j
    print(type(x))
    x = 35e3
    print(type(x))
    return 0

if __name__ == "__main__":
    main()

