arr=[1,2,3,2,4,4,4]
frequency={}
for i in arr:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
max_freq=0
element_max=None
for element in frequency:
    if (frequency[element]>max_freq):
        element_max=frequency[element]
        element_max=element
print("element with maximum frequency is:",element_max)
    