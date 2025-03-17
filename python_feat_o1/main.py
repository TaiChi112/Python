

def main()->int:
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
    return 0

if __name__ == "__main__":
    main()

