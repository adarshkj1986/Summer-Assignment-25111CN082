
first=int(input("enter the first limit"))

second=int(input("enter the second limit"))
print("the prime no  from first to last")
for n in range(first,second+1):
    if n>1:


        for i in range(2,n):


            if(n%i==0):
                
                break
        else:
            print(n,end=" ")
