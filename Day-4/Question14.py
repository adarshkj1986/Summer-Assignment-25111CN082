n=int(input("enter the number:"))
a=0
b=1
if(n==1):
    print(0)
elif(n==2):
    print(1)
for i in range(n-2): 
     next_term=a+b        #max_term=0+1
     a=b                  #a=1
     b=next_term          #b=1 and this same will continue till range n-2
print(b)
