def intersection_array(arr1,arr2):
    arr1.sort()
    arr2.sort()
    i,j=0,0
    intersection=[]
    while(i<len(arr1) and j<len(arr2)):
        if arr1[i]<arr2[j]:
            i+=1
        elif arr2[j]<arr1[i]:
            j+=1
        else:
            if not intersection or intersection[-1]!=arr1[i]:
                intersection.append(arr1[i])
            i+=1
            j+=1
    return intersection
arr1=[1,2,3,4,5,6]
arr2=[1,7,8,4,9]
result=intersection_array(arr1,arr2)
print(result)