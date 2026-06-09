arr=[1,2,2,3,3,3,4,4,5,5]
d=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            found=False
            for n in d:
                if n==arr[i]:
                    found=True
                    break
            if not found:
                d.append(arr[i])
print("duplicate elements are:",d)    