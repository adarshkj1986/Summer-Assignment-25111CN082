n=5
for i in range(1,n+1):        # 1,2,3,4,5
    for j in range(65,i+65):  # A value is 65
        print(chr(j),end="")  # the pattern will be printed
    print()