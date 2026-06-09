arr=[1,2,3,5,4,7]
arr.sort()
largest=arr[0]
for i in range(1,len(arr)):
    if(arr[i]>largest):
        largest=arr[i]
print("largest is:",largest)
second_largest=-1
for i in range(1,len(arr)):
    if(arr[i]>second_largest and arr[i]!=largest):
        second_largest=arr[i]
print("second largest element is:",second_largest)