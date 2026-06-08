arr=[3,5,6,7,8,10]
count_even=0
count_odd=0
for n in arr:

    if(n%2==0):
     count_even+=1
    else:
     count_odd+=1
print("even count is:",count_even)
print("odd count is:",count_odd)
