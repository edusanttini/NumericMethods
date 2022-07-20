from MatFunctions import *
import numpy as np


def print_mat(title, mat):
    print(title)
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j], end="  ")
        print()


def print_mat_numpy(mat):
    print("NumPy Result: ")
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j], end="  ")
        print()


def get_constant():
    return int(input("What is the constant you would like to multiply your matrix for?"))


def __get_mat(title, m):
    print("\nForneça os dados para ", title)
    for i in range(len(m)):
        print(f"Dados para linha {i}:")
        for j in range(len(m[i])):
            m[i][j] = int(input(f"   {title}[{i}][{j}]:"))


def get_matrix(title):
    row, col = get_dimension(title)
    mat_a = create_mat(row, col)
    __get_mat(title, mat_a)
    return mat_a


def get_dimension(title):
    print("\nForneça os dados para", title)
    row = int(input(f"Qtde de linhas da {title}: "))
    col = int(input(f"Qtde de colunas da {title}: "))
    return row, col
