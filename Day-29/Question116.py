inventory={}
while True:
    print("1. add item")
    print("2. remove item")
    print("3. check stock level")
    print("4. view")
    print("5. exit")
    ch=input("enter the choices from(1-5)")
    if ch=="1":
        item=input("enter the item name:")
        qty=int(input("enter the quantity:"))
        inventory[item]=qty
        print(f"updated:{item} set to {qty}")
    elif ch=="2":
        item=input("enter item to be removed:")
        if item in inventory:
            del inventory[item]
            print(f"removed {item} from inventory")
        else:
            print("item not found")
    elif ch=="3":
        item=input("enter item name:")
        if item in inventory:
            print(f"current stock of {item}:{inventory[item]}")
        else:
            print("not found")
    elif ch=="4":
        if not inventory:
            print("inventory is empty")
        else:
            for item,qty in inventory.items():
                print(f"{item}:{qty}")
    elif ch=="5":
        break
    else:
        print("invalid")