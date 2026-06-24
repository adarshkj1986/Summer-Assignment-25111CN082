matrix1=[[1,2],
         [5,10]]

result=[[0,0],
        [0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
     result[j][i]=matrix1[i][j]
for row in result:
   print(row)
