n=int(input("enter the number:"))
fib=[0,1]

for i in range(2,n):              #here range is 2 because fib is already having 2 values
    next_number=fib[-1]+fib[-2]
    fib.append(next_number)       #in this values like 0+1=1,1+1=2 will get stored
print(fib)
    