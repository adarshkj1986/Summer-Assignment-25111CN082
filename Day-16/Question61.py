arr=[1,2,4,5,6,7,8,9,10]
n=len(arr)
n1=int(input("enter the first n munbers:"))
for i in range(1,n1+1):
    sum=n1*(n1+1)//2
sum_2=0
for i in range(0,len(arr)):
    sum_2+=arr[i]
missing_number=sum-sum_2
print("missing number is:",missing_number)