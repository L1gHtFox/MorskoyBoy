import random

class half_of_ship():

    def __init__(self, symb, x, y):
        self.symb = symb
        self.x = x
        self.y = y

class ship():
    # Схип, ёпта
    def __init__(self, paluba):
        self.paluba = paluba

test = half_of_ship("2", 2, 2)

def zer_matrix(matrix):
    for i in range(10):
        new_matr = []
        for j in range(10):
            new_matr.append("~")
        matrix.append(new_matr)

def show_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # ВНИМАНИЕ КОСТЫЛЬ ВНИМАНИЕ
            if type(matrix[i][j]) == type(test):
                # ВНИМАНИЕ КОСТЫЛЬ ВНИМАНИЕ
                print(matrix[i][j].symb, end=' ')
            else:
                print(matrix[i][j], end=' ')
        print()