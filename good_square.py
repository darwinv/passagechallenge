def is_good_square(row, col, size, matrix):
    for i in range(row, row + size):
        for j in range(col, col + size):
            # print("i: j: ", i, j)
            if matrix[i][j] == 0:
                return False
    return True


def count_good_squares(matrix):
    dim = len(matrix)
    count = 0

    for i in range(dim):

        for j in range(dim):
            print("i, j: ", i , j)
            # Try to form squares starting from this cell
            for size in range(1, min(dim - i, dim - j) + 1):
                if is_good_square(i, j, size, matrix):
                    count += 1
                else:
                    break
    return count


def is_rows_equals_cols(matrix):
    num_rows = len(matrix)
    if num_rows == 0:
        return False # it's empty

    num_cols = len(matrix[0])
    return num_rows == num_cols



# Example usage:
matrix_ex = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
]

if __name__ == '__main__':
    if is_rows_equals_cols(matrix_ex):
        total_good_squares = count_good_squares(matrix_ex)
        print(total_good_squares)
