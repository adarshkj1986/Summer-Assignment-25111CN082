students={}
print("____welcome to the marksheet generation system____")
while True:
    print("menu")
    print("1. add student marks")
    print("2. view marksheets")
    print("3. exit")
    ch=input("enter your choices(1-3)")
    if ch=="1":
        roll=input("enter roll number:")
        name=input("enter student name:")
        m=int(input("enter the math marks:"))
        p=int(input("enter the physics marks:"))
        e=int(input("enter the english marks"))
        students[roll]={"name":name,"maths":m,"physics":p,"english":e}
        print("marks added successfully")
    elif ch=="2":
        if not students:
            print("no record found")
        else:
            for roll,data in students.items():
                total=data["maths"]+data["physics"]+data["english"]
                percentage=(total/300)*100
                print(f"roll:{roll} | name:{data["name"]}")
                print(f"maths: {data["maths"]} | physics:{data["physics"]} | english:{data["english"]}")
                print(f"total:{total}/300| percentage:{percentage}")
    elif ch=="3":
        print("exiting system")
        break
    else:
     print("invalid")
