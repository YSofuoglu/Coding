'''
The longest diagonals of a square matrix are defined as follows:

the first longest diagonal goes from the top left corner to the bottom right one;
the second longest diagonal goes from the top right corner to the bottom left one.
Given a square matrix, your task is to reverse the order of elements on both of its longest diagonals.

Example

For

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
the output should be

solution(matrix) = [[9, 2, 7],
                    [4, 5, 6],
                    [3, 8, 1]]
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer matrix

Guaranteed constraints:
1 ≤ matrix.length ≤ 100,
matrix.length = matrix[i].length,
1 ≤ matrix[i][j] ≤ 105.

[output] array.array.integer

Matrix with the order of elements on its longest diagonals reversed.
'''
def f(m):
    for i in range(len(m)//2):
        m[i][i], m[-i-1][-i-1] = m[-i-1][-i-1], m[i][i]
        m[i][-i-1], m[-i-1][i] = m[-i-1][i], m[i][-i-1]
    return m
