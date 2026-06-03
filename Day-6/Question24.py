x=int(input("enter the number in base:"))
bin=int(input("enter the number in power:"))
ans=1
while(bin>0):
    if(bin%2==1):
        ans=ans*x
    x=x*x
    bin=bin//2
print("answer is:",ans)

