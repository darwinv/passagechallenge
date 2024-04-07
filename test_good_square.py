import unittest
import good_square


matrix_empty = []

matrix_3 = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
]

matrix_2 = [
    [1, 1],
    [1, 1],
]

matrix_2_b = [
    [1, 1],
    [1, 0],
]

matrix_3_b = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
]

matrix_3_c = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 0],
]

matrix_n_x_m = [
    [1, 1, 1],
    [1, 1, 1],
]

matrix_4 = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]


class TestRowsEqualsCols(unittest.TestCase):

    def test_matrix_x3(self):

        result = good_square.is_rows_equals_cols(matrix_3)
        self.assertEqual(result, True)

    def test_matrix_x2(self):

        result = good_square.is_rows_equals_cols(matrix_2)
        self.assertEqual(result, True)

    def test_matrix_n_x_m(self):

        result = good_square.is_rows_equals_cols(matrix_n_x_m)
        self.assertEqual(result, False)

    def test_matrix_empty(self):

        result = good_square.is_rows_equals_cols(matrix_empty)
        self.assertEqual(result, False)


class TestCountGoodSquares(unittest.TestCase):

    def test_matrix_x3(self):
        result = good_square.count_good_squares(matrix_3)
        self.assertEqual(result, 14)

    def test_matrix_x2(self):
        result = good_square.count_good_squares(matrix_2)
        self.assertEqual(result, 5)

    def test_matrix_x2_b(self):
        result = good_square.count_good_squares(matrix_2_b)
        self.assertEqual(result, 3)

    def test_matrix_x3_b(self):
        result = good_square.count_good_squares(matrix_3_b)
        self.assertEqual(result, 8)

    def test_matrix_x3_c(self):
        result = good_square.count_good_squares(matrix_3_c)
        self.assertEqual(result, 11)

    def test_matrix_x4_c(self):
        result = good_square.count_good_squares(matrix_4)
        self.assertEqual(result, 30)
