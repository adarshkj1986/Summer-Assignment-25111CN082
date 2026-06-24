def is_symetrical(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            if (matrix[i][j]!=matrix[j][i]):
                return False
    return True
matrix_a=[[1,2,3],          # this is a symmetric matrix
          [2,4,5],
          [3,5,6]]
matrix_b=[[1,2,3],          # this is not a symmetric matrix
         [4,5,6],
         [7,8,9]]
print("is matix_a symmetrical:",is_symetrical(matrix_a))   # output will be true
print("is matix_b symmetrical:",is_symetrical(matrix_b))   # output will be false