balance=1000
while True:
    print("------ATM-----")
    print("1.check balance")
    print("2.deposit money")
    print("3.withdraw money")
    print("4.exit")
    ch=int(input("enter the choices from(1-4)"))
    if ch==1:
        print("your balance is:",balance)

    elif ch==2:
        money=int(input("enter the amount to be deposited:"))
        balance+=money
    elif ch==3:
        withdraw=int(input("enter the money to withdraw:"))
        balance=balance-withdraw
    elif ch==4:
        print("thank you for using our ATM")
        break
    else:
        print("invalid")