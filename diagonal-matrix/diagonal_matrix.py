def diagonal_sums(matrix):
    '''
    Calculates the sum of each diagonal in a given square matrix

    Args:
        matrix: represents a square matrix containing numbers
    
    Returns:
        tuple: containing the sums of each diagonal in the given matrix
    '''
    diagonal_left_right_sum = 0
    diagonal_right_left_sum = 0

    for i in range(len(matrix)):
        diagonal_left_right_sum += matrix[i][i]
        diagonal_right_left_sum += matrix[i][-(i+1)]
    return (diagonal_left_right_sum, diagonal_right_left_sum)

def diagonal_sums_adiff(matrix):
    '''
    Calculates the absolute difference between the sums of the diagonals in a given square matrix

    Args:
        matrix: represents a square matrix containing numbers
    
    Returns:
        int/long/float: the absolute difference between the sums of the diagonals in the given square matrix
    '''
    sums = diagonal_sums(matrix)
    return abs(sums[0] - sums[1])

if __name__ == '__main__':
    matrix_a = [[1, 2, 3],
                [2, 3, 1],
                [3, 2, 1]]
    assert diagonal_sums_adiff(matrix_a) == 4
    
    matrix_b = [[1, 2], 
                [3, 2]]
    assert diagonal_sums_adiff(matrix_b) == 2
    
    matrix_c = []
    assert diagonal_sums_adiff(matrix_c) == 0
