def armstrong(n):    # 153 is armstrong as 1**3+5**3+3**3 is equals to the number n
    count=0
    n1=n
    sum=0
    while(n>0):
        n=n//10
        count=count+1
    n=n1
    while(n>0):
        r=n%10
        sum=sum+pow(r,count)
        n=n//10
    if(n1==sum):
        print("this is a armstrong number")
    else:
        print("this is not a armstrong number")
armstrong(153)
    

    