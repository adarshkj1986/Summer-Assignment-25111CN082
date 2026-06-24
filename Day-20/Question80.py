matrix=[[1,2,3],
        [5,7,8],
        [7,9,4]]
for j in range(len(matrix[0])):
    sum_col=0
    for i in range(len(matrix)):
        sum_col+=matrix[i][j]
    print("the column  wise sum is:",sum_col)