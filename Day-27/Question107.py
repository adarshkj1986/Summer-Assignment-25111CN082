salary={}
print("_______welcome to the salary management system____")
while True:
    print("menu")
    print("1. add salary")
    print("2. view all salaries")
    print("3.exit")

    ch=input("enter the choices from (1-3)")
    if ch=="1":
        emp_id=input("enter employee ID:")
        salaries=input("enter the salary:")
        salary[emp_id]=salaries
        print(f"salaries for{emp_id} updated successfully")
    elif ch=="2":
        if not salary:
            print("no salary records found")
        else:
            for emp_id,salaries in salary.items():
                print(f"employee ID:{emp_id} | salary:{salary}")
    elif ch=="3":
        print("exit the system")
        break
    else:
        print("invalid")
        