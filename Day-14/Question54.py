n=[1,2,3,4,5,4,6,5,5]
frequency={}
for i in n:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
for element in frequency:
    print(element,":",frequency[element])