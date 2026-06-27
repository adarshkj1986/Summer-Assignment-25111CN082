contacts={}
while True:
    print("1. add contact")
    print("2. search contact")
    print("3. delete contact")
    print("4. view all contacts")
    print("5. exit")
    ch=input("enter the choices from(1-5)")
    if ch=="1":
        name=input("enter the name:")
        phone=input("enter the phone number:")
        contacts[name]=phone
        print(f"contact for{name} is saved")
    elif ch=="2":
        name=input("enter the name to be search")
        if name in contacts:
            print(f"phone number for {name}: {contacts[name]}")
        else:
            print("contact not found")
    elif ch=="3":
        name=input("enter the name to be deleted")
        if name in contacts:
            del contacts[name]
            print(f"contact for {name} is  deleted")
        else:
            print("contact not found")
    elif ch=="4":
        print("____all contacts are____")
        if not contacts:
            print("no contact stored")
        else:
            for name,phone in contacts.items():
                print(f"{name}:{phone}")
    elif ch=="5":
        print("exiting system")
        break
    else:
        print("invalid")