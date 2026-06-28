my_array=[]
while True:
    print("1. add element")
    print("2. remove element")
    print("3. view all elements")
    print("4. exit")
    ch=input("enter the choices from(1-4)")
    if ch=="1":
        element=input("enter the value to add:")
        my_array.append(element)
        print(f"added {element} to the array")
    elif ch=="2":
        element=input("enter the value to remove:")
        if element in my_array:
            my_array.remove(element)
            print(f"removed {element} from array")
        else:
            print("element not found")
    elif  ch=="3":
        print(f"current array:{my_array}")
    elif ch=="4":
        print("exit")
        break
    else:
        print("invalid")
    