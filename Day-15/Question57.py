def reverse(arr):
    n=len(arr)
    l=0
    r=len(arr)-1
    while(l<r):
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
arr=[1,2,6,7,8,4,3]

reverse(arr)
print("reverse array is:",arr)