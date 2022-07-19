from MatFunctions import *
import numpy as np


def print_mat(title, m):
    print(title)
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end="  ")
        print()


def print_python_result(result):
    print("Python Result: \n")
    for i in range(len(result)):
        for j in range(len(result[i])):
            print(result[i][j], end="  ")
        print()


def print_numpy_result(result):
    print("NumPy Result: \n", result)


def __get_mat(title, m):
    print("\nForneça os dados para ", title)
    for i in range(len(m)):
        print(f"Dados para linha {i}:")
        for j in range(len(m[i])):
            m[i][j] = int(input(f"   {title}[{i}][{j}]:"))


def get_matrix(title, is_numpy):
    row, col = get_dimension(title)
    if is_numpy:
        mat_a = np.ndarray(shape=(row, col), dtype=int)
    else:
        mat_a = create_mat(row, col)
    __get_mat(title, mat_a)
    return mat_a


def get_numpy_matrix(title):
    row, col = get_dimension(title)

    __get_mat(title, mat_a)
    return mat_a


def get_dimension(title):
    print("\nForneça os dados para", title)
    row = int(input(f"Qtde de linhas da {title}: "))
    col = int(input(f"Qtde de colunas da {title}: "))
    return row, col
