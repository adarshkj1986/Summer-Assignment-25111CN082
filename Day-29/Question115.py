user_string=""
while True:
    print("1. set/change string")
    print("2. reverse string")
    print("3. convert to uppercase")
    print("4. convert to lowercase")
    print("5. exit")
    ch=input("enter your choice from(1-5)")
    if ch=="1":
        user_string=input("enter the string:")
        print("string updated")
    elif ch=="2":
        user_string=user_string[::-1]
        print("string reversed")
    elif ch=="3":
        user_string=user_string.upper()
        print("string is converted")
    elif ch=="4":
        user_string=user_string.lower()
        print("string is converted")
    elif ch=="5":
        break
    else:
        print("invalid")