while True:
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. exit")
    ch=input("enter the choices from(1-5)")
    if ch=="5":
        print("exit")
        break
    if ch in ("1","2","3","4"):
        n1=float(input("enter the first number"))
        n2=float(input("enter the second number"))
        if ch=="1":
            print("add two numbers")
            sum=n1+n2
            print("the sum is:",sum)
        elif ch=="2":
            print("subtract two numbers")
            sub=n1-n2
            print("subtract is:",sub)
        elif ch=="3":
            print("multiply two numbers")
            multi=n1*n2
            print("multiplication is:",multi)
        elif ch=="4":
            print("divide two numbers")
            div=n1//n2
            print("after divide:",div)
        else:
            print("error")
    else:
        print("invalid")