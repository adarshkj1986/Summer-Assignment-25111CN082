employees={}
print("_______welcome to the employee management system____")
while True:
    print("menu")
    print("1. add employee")
    print("2. view all employee")
    print("3.exit")

    ch=input("enter the choices from (1-3)")
    if ch=="1":
        emp_id=input("enter employee ID:")
        name=input("enter name:")
        role=input("enter role:")
        salary=input("enter the salary:")
        employees[emp_id]={
            "name":name,
            "role":role,
            "salary":salary
            }
        print("employee added")
    elif ch=="2":
        if not employees:
            print("the list is empty")
        else:
            for emp_id,info in employees.items():
                print(f"ID:{emp_id} | Name:{info["name"]} | Role:{info["role"]} | salary:{info["salary"]}")
    elif ch=="3":
        break
    else:
        print("invalid")