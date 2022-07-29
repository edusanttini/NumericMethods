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


def multiply_mat():
    mat_a = get_matrix("Matrix A")
    mat_b = get_matrix("Matrix B")
    if len(mat_a) == len(mat_b[0]):
        print_mat("Matriz A", mat_a)
        print_mat("Matriz B", mat_b)
        print_mat("Matriz R = A * B", matrix_product(mat_a, mat_b))
        print_mat_numpy(np.matmul(np.array(mat_a), np.array(mat_b)))
    else:
        print(f"Coluna de A {len(mat_a)} é diferente da linha de B {len(mat_b[0])}. Não posso multiplicar!")


def scalar_matrix_product():
    mat_a = get_matrix("Matrix A")
    k = get_constant()
    print_mat("Matrix R * K =", scalar_product(mat_a, k))
    print_mat_numpy(np.dot(np.array(mat_a), k))


def third_case():
    mat_a = get_matrix("Matrix A")
    print("Min Result: ", min_matrix_element(mat_a))
    print("Max Result: ", max_matrix_element(mat_a))
    print("Sum Result: ", sum_matrix(mat_a))
    print("Min Result numPy: ", np.min(np.array(mat_a)))
    print("Max result numPy: ", np.max(np.array(mat_a)))
    print("Sum result numPy: ", np.sum(np.array(mat_a)))


def matrix_determinant(size):
    if size == 3:
        mat_a = get_hardcoded_matrix("Matrix A", size)
        print("NumPy Result: \n", np.linalg.det(mat_a))
        print("Result: \n", get_matrix_determinant(mat_a))
    else:
        mat_a = get_hardcoded_matrix("Matrix A", size)
        print("NumPy Result: \n", np.linalg.det(mat_a))
        print("Result: \n", get_matrix_determinant(mat_a))


def matrix_transpose():
    mat_a = get_matrix("Matrix A")
    print_mat("Matrix A", get_matrix_transpose(mat_a))
    print_mat_numpy(np.transpose(np.array(mat_a)))


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
            matrix_determinant(3)
        case 5:
            matrix_determinant(4)
        case 6:
            matrix_transpose()
        case default:
            print("wrong option nerd")
    input("Press Enter to continue.")
