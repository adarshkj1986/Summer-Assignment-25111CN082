n=[23,45,56,78,89]
def linear_search(n,target):
    for i in range(len(n)):
        if n[i]==target:
            return i
    return -1
print(linear_search(n,78))
