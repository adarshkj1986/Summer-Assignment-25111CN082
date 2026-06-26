while True:
    print("WELCOME TO THE CRICKET QUIZ")

    print("1)what is the highest score in odi cricket by a player:")

    print("2)most no of centuries by a player:")

    print("3) exit")
    ch=int(input("enter the no(1-3):"))
    if ch==1:
        print("a)200")

        print("b)100")

        print("c)500")

        print("d)264")

        h=input("enter the choice from(a-d):")

        if(h=="d"):

            print("your answer is correct")
        else:

            print("not correct")
        
        
    elif ch==2:
        print("a)Virat Kholi")

        print("b)Sachine Tendulkar")

        print("c)rohit sharma")

        print("d)mahendra singh dhoni")

        h=input("enter the choice from(a-d):")
        if(h=="b"):

            print("your answer is correct")
        else:

            print("not correct")


    elif ch==3:
        break

    else:
        print("invalid")