import numpy as np


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


def scalar_product(mat_a, k):
    row = len(mat_a)
    col = len(mat_a[0])
    final_mat = create_mat(row, col)
    for i in range(row):
        for j in range(col):
            final_mat[i][j] = mat_a[i][j] * k
    return final_mat


def min_matrix_element(mat_a):
    row = len(mat_a)
    col = len(mat_a[0])
    result = mat_a[0][0]
    for i in range(row):
        for j in range(col):
            if mat_a[i][j] < result:
                result = mat_a[i][j]
    return result


def max_matrix_element(mat_a):
    row = len(mat_a)
    col = len(mat_a[0])
    result = mat_a[0][0]
    for i in range(row):
        for j in range(col):
            if mat_a[i][j] > result:
                result = mat_a[i][j]
    return result


def sum_matrix(mat_a):
    row = len(mat_a)
    col = len(mat_a[0])
    result = 0
    for i in range(row):
        for j in range(col):
            result = result + mat_a[i][j]
    return result


def get_positive_diagonal_values(mat_a, row, col):
    main_diag = sec_diag = third_diag = 1
    for i in range(row):
        for j in range(col):
            if i == j:
                main_diag = main_diag * mat_a[i][j]
            elif i == 0 and j == 2\
                    or i == 1 and j == 0\
                    or i == 2 and j == 1:
                sec_diag = sec_diag * mat_a[i][j]
            elif i == 0 and j == 1\
                    or i == 1 and j == 2\
                    or i == 2 and j == 0:
                third_diag = third_diag * mat_a[i][j]
    return main_diag + sec_diag + third_diag


def get_negative_diagonal_values(mat_a, row, col):
    fourth_diag = fifth_diag = sixth_diag = 1
    for i in range(row):
        for j in range(col):
            if i == 0 and j == 2 \
                    or i == 1 and j == 1 \
                    or i == 2 and j == 0:
                fourth_diag = fourth_diag * mat_a[i][j]
            elif i == 0 and j == 1 \
                    or i == 1 and j == 0 \
                    or i == 2 and j == 2:
                fifth_diag = fifth_diag * mat_a[i][j]
            elif i == 0 and j == 0 \
                    or i == 1 and j == 2 \
                    or i == 2 and j == 1:
                sixth_diag = sixth_diag * mat_a[i][j]
    return fourth_diag + fifth_diag + sixth_diag


def remove_row(mat_a):
    print("TODO - remove row for laplace rule")
    return mat_a


def remove_col(mat_a):
    print("TODO - remove col for laplace rule")
    return mat_a


def get_matrix_determinant(mat_a):
    row = len(mat_a)
    col = len(mat_a[0])
    if row == 4 and col == 4:
        remove_row(mat_a)
        remove_col(mat_a)
    positive_diag = get_positive_diagonal_values(mat_a, row, col)
    negative_diag = get_negative_diagonal_values(mat_a, row, col)
    return positive_diag - negative_diag


def get_matrix_transpose(mat_a):
    row = len(mat_a)
    col = len(mat_a[0])
    final_mat = create_mat(row, col)
    for i in range(row):
        for j in range(col):
            if i == j:
                final_mat[i][j] = mat_a[i][j]
            else:
                final_mat[i][j] = mat_a[j][i]
    return final_mat
