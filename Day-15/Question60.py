arr=[1,2,0,3,0,5,0,0,4]
j=-1
for i in range(0,len(arr)):
    if(arr[i]==0):
        j=i
        break
for i in range(j+1,len(arr)):
    if(arr[i]!=0):
        arr[i],arr[j]=arr[j],arr[i]
        j+=1
print("the array is",arr)