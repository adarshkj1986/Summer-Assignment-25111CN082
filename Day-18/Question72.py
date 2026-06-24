def selection_sort_dec(a):
    n=len(a)
    for i in range(n):
        min_e=i    #minimum element in the array
        for j in range(i+1,n):
            if a[j]>a[min_e]:
                min_e=j
        a[i],a[min_e]=a[min_e],a[i]
    return a
a=[5,4,2,6,1]
sorted_array=selection_sort_dec(a)
print("sorted array in descending order is:",sorted_array)