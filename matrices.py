# Script for some basic matrix computations
class Matrices(object):

    matrix = []

    def __init__(self, matrix_size):
        '''Initialise a matrix list and it\'s size attribute'''
        self.matrix_size = matrix_size

    def get_matrix_elements(self, matrix_size=''):
        '''Input matrix elements depending on size'''
        if self.matrix_size:
            self.matrix_size = 9
            for i in range(self.matrix_size):
                self.matrix.append(int(input("Enter the element: ")))
            return self.matrix
        else:
            self.matrix_size = 4
            for i in range(self.matrix_size):
                self.matrix.append(int(input("Enter the element: ")))
            return self.matrix

    def determinant(self, matrix):
        '''Method to calculate the determinant'''
        det = 0
        lead_diag = 0
        other_diag = 0
        sub_a = 0
        sub_b = 0
        sub_c = 0
        if self.matrixSize == 4:
            lead_diag = (self.matrix[0] * self.matrix[3])
            other_diag = (self.matrix[1] * self.matrix[2])
            det = lead_diag - other_diag
            return det
        elif self.matrix_size == 9:
            ''' My implementation of method on
            https://www.mathsisfun.com/algebra/matrix-determinant.html'''
            sub_a = self.matrix[0] * (self.determinant([self.matrix[4],
                                                        self.matrix[5],
                                                        self.matrix[7],
                                                        self.matrix[8]]))

            sub_b = self.matrix[1] * (self.determinant([self.matrix[3],
                                                        self.matrix[5],
                                                        self.matrix[6],
                                                        self.matrix[8]]))

            sub_c = self.matrix[2] * (self.determinant([self.matrix[3],
                                                        self.matrix[5],
                                                        self.matrix[6],
                                                        self.matrix[8]]))
            det = sub_a - sub_b + sub_c

        return det


a = Matrices(4)
a.get_matrix_elements()
print(a.determinant())