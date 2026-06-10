def rotate_array(a,k):
    n=len(a)
    if n==0:
        return a
    k=k%10
    return a[-k:]+a[:-k]
arr=[1,2,3,4,5]
k=2
new_array=rotate_array(arr,k)
print(new_array)