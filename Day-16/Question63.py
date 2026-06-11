def pair(n,target):
    seen=set()
    for num in n:
        complement=target-num
        if(complement in seen):
            return(complement,num)
        seen.add(num)
    return None
list=[10,15,3,7]
target=17
result=pair(list,target)
if result:
    print("pair found",result)
else:
    print("not found")