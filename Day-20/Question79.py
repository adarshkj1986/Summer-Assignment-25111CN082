matrix=[[1,2,3],
        [5,7,8],
        [7,9,4]]
for i in range(len(matrix)):
    sum_row=0
    for j in range(len(matrix[i])):
        sum_row+=matrix[i][j]
    print("the row wise sum is:",sum_row)