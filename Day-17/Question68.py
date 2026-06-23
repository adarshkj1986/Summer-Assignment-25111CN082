def common_elements(arr1,arr2):
    arr1.sort()
    arr2.sort()
    i,j=0,0
    common=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            i+=1
        elif arr2[j]<arr1[i]:
            j+=1
        else:
            if not common or common[-1]!=arr1[i]:
                common.append(arr1[i])
            i+=1
            j+=1
    return common
arr1=[1,2,3,4,5]
arr2=[2,3,4,7,8]
result=common_elements(arr1,arr2)
print("common elements are:",result)