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


def zeros_matrix(rows, cols):
    mat = []
    while len(mat) < rows:
        mat.append([])
        while len(mat[-1]) < cols:
            mat[-1].append(0.0)
    return mat


def copy_matrix(mat):
    rows = len(mat)
    cols = len(mat[0])
    matrix_copy = zeros_matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            matrix_copy[i][j] = mat[i][j]
    return matrix_copy


def get_any_matrix_determinant(mat):
    row = len(mat)
    new_matrix = copy_matrix(mat)
    for fd in range(row):
        for i in range(fd + 1, row):
            if new_matrix[fd][fd] == 0:
                new_matrix[fd][fd] == 1.0e-18
            if new_matrix[fd][fd] != 0:
                cr_scaler = new_matrix[i][fd] / new_matrix[fd][fd]
            for j in range(row):
                new_matrix[i][j] = new_matrix[i][j] - cr_scaler * new_matrix[fd][j]
    product = 1.0
    for i in range(row):
        product *= new_matrix[i][i]
    return product


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
