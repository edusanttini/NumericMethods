import numpy as np
from MatFunctions import *
from Utils import *
from Utils import __get_mat


def print_menu():
    print("Menu Option: ")
    print("  0 - sair")
    print("  1 - multiplicar matrizes")
    print("  2 - multiplicar matriz por escalar")
    print("  3 - Maior, menor e soma dos elementos da matriz")
    print("  4 - determinante matriz 3x3 (Regra de Sarrus)")
    print("  5 - determinante matriz 4x4 (Teorema de Laplace)")
    print("  6 - transposta de matriz")


def print_matrix(title, matrix):
    print("Matrix ", title, ": \n", matrix)


def multiply_mat():
    mat_a = get_matrix("Matrix A")
    mat_b = get_matrix("Matrix B")
    if len(mat_a) == len(mat_b[0]):
        print_mat("Matriz A", mat_a)
        print_mat("Matriz B", mat_b)
        print_mat("Matriz R = A * B", matrix_product(mat_a, mat_b))
        print_numpy_result(np.matmul(mat_a, mat_b))
    else:
        print(f"Coluna de A {len(mat_a)} é diferente da linha de B {len(mat_b[0])}. Não posso multiplicar!")


def get_constant():
    return int(input("What is the constant you would like to multiply your matrix for?"))


def scalar_matrix_product():#TODO create scalar procuct method by myself
    mat_a = get_matrix("Matrix A")
    result = np.dot(mat_a, get_constant())
    print("Result: \n", result)


def min_matrix_element(mat_a):#TODO create scalar procuct method by myself
    return np.min(mat_a)


def max_matrix_element(mat_a):#TODO create scalar procuct method by myself
    return np.max(mat_a)


def sum_matrix(mat_a):#TODO create scalar procuct method by myself
    return np.sum(mat_a)


def third_case():
    mat_a = get_matrix("Matrix A")
    print("Min result: \n", min_matrix_element(mat_a))
    print("Max result: \n", max_matrix_element(mat_a))
    print("Sum result: \n", sum_matrix(mat_a))


def matrix_determinant():
    mat_a = get_matrix("Matrix A")
    result = np.linalg.det(mat_a)
    print("Result: \n", result)


option = 1
while option != 0:
    print_menu()
    option = int(input("What is your option?"))
    match option:
        case 1:
            multiply_mat()
        case 2:
            scalar_matrix_product()
        case 3:
            third_case()
        case 4:
            matrix_determinant()
        case 5:
            get_numpy_matrix("oi")
        case default:
            print("wrong option nerd")