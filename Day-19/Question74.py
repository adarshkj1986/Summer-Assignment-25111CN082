matrix1=[[1,2],
         [5,10]]
matrix2=[[2,7],
         [6,7]]
result=[[0,0],
        [0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j]=matrix1[i][j]-matrix2[i][j]
for row in result:
    print(row)