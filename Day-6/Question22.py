bin=int(input("enter the no:"))       #1001
bin=int(bin)
dec,i=0,0
while(bin>0):                         #1001>0
    r=bin%10                          #1001%10=1
    exp=r*(2**i)                      #1*(2**0)
    dec=exp+dec                       #dec=1
    bin=bin//10
    i+=1                      #1001//10=100
    
print("decimal no is:",dec)
