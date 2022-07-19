def create_mat(row, col):
    matrix = row * [0]
    for i in range(row):
        matrix[i] = col * [0]
    return matrix


def matrix_product(mat_a, mat_b):
    row = len(mat_a)
    col = len(mat_b[0])
    final_mat = create_mat(row, col)
    for i in range(row):
        for j in range(col):
            for k in range(len(mat_b)):
                final_mat[i][j] = final_mat[i][j] + mat_a[i][j] * mat_b[k][j]
    return final_mat
