import copy
import math


class Matrix:

    def __init__(self, row_number, column_number, rows):
        self.row_number = row_number
        self.column_number = column_number
        self.rows = rows

        self.columns = []
        for i in range(self.column_number):
            self.columns.append([self.rows[j][i] for j in range(self.row_number)])

    def add_matrices(self, other_matrix):
        if self.row_number == other_matrix.row_number and self.column_number == other_matrix.column_number:
            print("The result is:")
            for i in range(self.row_number):
                row = [str(float(self.rows[i][j]) + float(other_matrix.rows[i][j]))
                       for j in range(self.column_number)]
                print(" ".join(row))
        else:
            print("ERROR")

    def scalar_multiplication(self, scalar):
        print("The result is:")
        for i in range(self.row_number):
            row = []
            for j in range(self.column_number):
                row.append(str(int(float(scalar) * float(self.rows[i][j]) * 100) / 100))
            print(" ".join(row))

    def multiply_matrices(self, other_matrix):
        if self.column_number == other_matrix.row_number:
            print("The result is:")
            for i in range(self.row_number):
                product_row = []
                for j in range(other_matrix.column_number):
                    product_row.append(0)
                    for k in range(len(self.rows[i])):
                        product_row[j] += self.rows[i][k] * other_matrix.columns[j][k]
                str_product_row = [str(product_row[m]) for m in range(len(product_row))]
                print(" ".join(str_product_row))

    def main_transposition(self):
        trans_rows = []
#        print("The result is:")
        for i in range(self.row_number):
            str_column = [str(self.columns[i][j]) for j in range(self.column_number)]
            trans_rows.append(self.columns[i])
#            print(" ".join(str_column))
        trans_matrix = Matrix(self.row_number, self.column_number, trans_rows)
        return trans_matrix

    def side_transposition(self):
        print("The result is:")
        for i in range(-1, -1 - self.row_number, -1):
            str_column = [str(self.columns[i][j]) for j in range(self.column_number)]
            str_column.reverse()
            print(" ".join(str_column))

    def vertical_transposition(self):
        print("The result is:")
        for i in range(self.row_number):
            str_row = [str(self.rows[i][j]) for j in range(self.column_number)]
            str_row.reverse()
            print(" ".join(str_row))

    def horizontal_transposition(self):
        print("The result is:")
        for i in range(self.row_number - 1, -1, -1):
            str_row = [str(self.rows[i][j]) for j in range(self.column_number)]
            print(" ".join(str_row))


def determinant(det_matrix):
    # Check if the matrix is square
    if det_matrix.row_number != det_matrix.column_number:
        print("Determinant is only defined for square matrices.")
    else:
        # Matrix 1 x 1
        if det_matrix.row_number == 1:
            return det_matrix.rows[0][0]
        # Matrix 2 x 2
        elif det_matrix.row_number == 2:
            return det_matrix.rows[0][0] * det_matrix.rows[1][1] - det_matrix.rows[0][1] * det_matrix.rows[1][0]
        else:
            determinant_value = 0

            for i in range(det_matrix.row_number):
                minor_rows = copy.deepcopy(det_matrix.rows)
                del minor_rows[0]

                for j in range(det_matrix.column_number - 1):
                    del minor_rows[j][i]
                minor_matrix = Matrix(det_matrix.row_number - 1, det_matrix.column_number - 1, minor_rows)
                determinant_value += det_matrix.rows[0][i] * math.pow(-1, i) * determinant(minor_matrix)

            return determinant_value


def cofactor(cof_matrix, i, j):
    cof_rows = copy.deepcopy(cof_matrix.rows)
    del cof_rows[i]
    for k in range(cof_matrix.row_number - 1):
        del cof_rows[k][j]
    new_matrix = Matrix(cof_matrix.row_number - 1, cof_matrix.column_number - 1, cof_rows)
    return math.pow(-1, i + j) * determinant(new_matrix)


def inverse_matrix(inv_matrix):
    if determinant(inv_matrix) == 0:
        print("This matrix doesn't have an inverse.")
    else:
        cof_rows = []
        for i in range(inv_matrix.row_number):
            cof_rows.append([])
            for j in range(inv_matrix.column_number):
                cof_rows[i].append(cofactor(inv_matrix, i, j))
        cof_matrix = Matrix(inv_matrix.row_number, inv_matrix.column_number, cof_rows)
        trans_cof_matrix = cof_matrix.main_transposition()
        trans_cof_matrix.scalar_multiplication(1 / determinant(inv_matrix))


# This function creates a Matrix from user input.
def create_matrix():
    row_number, column_number = (int(n) for n in input("Enter matrix size: ").split())
    print("Enter matrix: ")
    rows = []
    for i in range(row_number):
        rows.append([float(n) for n in input().split()])
    return Matrix(row_number, column_number, rows)


def menu():
    print('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit''')


while True:
    menu()
    user_choice = input("Your choice :")
    if user_choice == "1":
        matrix_1 = create_matrix()
        matrix_2 = create_matrix()
        matrix_1.add_matrices(matrix_2)
    elif user_choice == "2":
        matrix = create_matrix()
        scalar = input("Enter constant: ")
        matrix.scalar_multiplication(scalar)
    elif user_choice == "3":
        matrix_1 = create_matrix()
        matrix_2 = create_matrix()
        matrix_1.multiply_matrices(matrix_2)
    elif user_choice == "4":
        print('''1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line''')
        transpose_choice = input("Your choice:")
        matrix = create_matrix()
        if transpose_choice == "1":
            print("The result is:")
            for tr_row in matrix.main_transposition().rows:
                str_row = [str(tr_row[j]) for j in range(len(tr_row))]
                print(" ".join(str_row))
        elif transpose_choice == "2":
            matrix.side_transposition()
        elif transpose_choice == "3":
            matrix.vertical_transposition()
        elif transpose_choice == "4":
            matrix.horizontal_transposition()
    elif user_choice == "5":
        matrix = create_matrix()
        print("The result is:")
        print(determinant(matrix))
    elif user_choice == "6":
        matrix = create_matrix()
        inverse_matrix(matrix)
    elif user_choice == "0":
        break
