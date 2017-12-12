import unittest
from matrices import Matrices


class TestMatrices(unittest.TestCase):

    def setUp(self):
        '''Create matrix objects to be used in all tests'''
        self.first_matrix_size = 4
        self.first_matrix_elements = [1, 2, 3, 4]
        self.second_matrix_size = 9
        self.second_matrix_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.first_matrix = Matrices(self.first_matrix_size,
                                     self.first_matrix_elements)

        self.second_matrix = Matrices(self.second_matrix_size,
                                      self.second_matrix_elements)

    def test_input_type(self):
        '''Does the method only accept integer numbers?'''

        # Check if all elements are integers
        for i in range(self.first_matrix_size):
            for j in range(self.second_matrix_size):
                self.assertEqual(type(self.first_matrix_elements[i]), int)
                self.assertEqual(type(self.second_matrix_elements[j]), int)

    def test_number_of_elements(self):
        '''Do we have the correct number of elements for the matrix?'''
        try:
            self.assertEqual(len(self.first_matrix_elements), 4)
            self.assertEqual(len(self.second_matrix_elements), 9)
        except IndexError:
            print("Incorrect number of elements")

    def test_default_matrix_size(self):
        '''Does the method work by default for 2x2 matrices?'''
        self.first_matrix.get_matrix_elements()
        self.assertEqual(self.first_matrix.get_matrix_elements(),
                         self.first_matrix_elements)

    def test_custom_matrix_size(self):
        '''Does the method work for 3x3 matrices?'''
        self.second_matrix.get_matrix_elements(9)
        self.assertEqual(self.second_matrix.get_matrix_elements(),
                         self.second_matrix_elements)

    def test_two_by_two_det(self):
        '''Does the determinant accurately compute for 2x2 matrices?'''
        two_by_two_det = self.first_matrix.determinant(
            self.first_matrix_elements)
        self.assertEqual(two_by_two_det, -2)

    def test_three_by_three_det(self):
        '''Does the determinant accurately compute for 3x3 matrices?'''


unittest.main()
