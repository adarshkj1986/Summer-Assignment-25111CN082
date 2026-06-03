def convertbinary(n):
    if n>1:
        convertbinary(n//2)
    print(n%2,end="")
print("binary of this decimal no is:")
convertbinary(int(input("enter the no:")))