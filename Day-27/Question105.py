students={}
while True:
    print("Menu")
    print("1. add student")
    print("2. view students")
    print("3. exit")
    ch=input("enter the choices from(1-3)")
    if ch=="1":
        st_id=input("enter the student id:")
        name=input("enter the student name:")
        students[st_id]=name
        print("student added")
    elif ch=="2":
        print("current student:")
        if len(students)==0:
            print("list empty")
        else:
            for id_key in students:
                print(f"ID:{id_key} | Name:{students[id_key]}")
    elif ch=="3":
        print("break")
        break
    else:
        print("invalid")