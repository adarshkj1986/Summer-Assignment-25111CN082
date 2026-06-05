n=5
for i in range(1,n+1):      # 1,2,3,4,5
    for j in range(1,i+1):  # 1,2 1 element , 1,3 2 elements till 5 elements
        print(j,end="")     # then the pattern will be printed
    print()