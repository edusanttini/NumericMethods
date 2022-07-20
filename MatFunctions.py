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
