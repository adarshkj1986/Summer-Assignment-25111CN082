student_names=[]
student_grades=[]
while True:
    print("1. add student record")
    print("2. remove student record")
    print("3. view all records")
    print("4. exit")
    ch=input("enter your choice(1-4)")
    if ch=="1":
        name=input("enter your name:")
        grade=input("enter student grades:")
        student_grades.append(grade)
        student_names.append(name)
        print(f"record added for {name}")
    elif ch=="2":
        name=input("enter the name of student to removed:")
        if name in student_names:
            index=student_names.index(name)
            student_names.pop(index)
            student_grades.pop(index)
            print(f"record for {name} removed")
        else:
            print("student not found")
    elif ch=="3":
        if not student_names:
            print("no records")
        else:
            for i in range(len(student_names)):
                print(f"{i+1} name:{student_names[i]},grade:{student_grades[i]}")
    elif ch=="4":
        break
    else:
        print("invalid")

