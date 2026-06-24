def binary_search(a,target):
    n=len(a)
    l=0
    r=n-1
    while(l<=r):
        middle=(l+r)//2
        if a[middle]==target:
            return middle
        elif(a[middle]<target):
            l=middle+1
        else:
            r=middle-1
    return -1
a=[12,23,34,45,56,78,89]
print(binary_search(a,56))