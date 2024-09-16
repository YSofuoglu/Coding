'''
Given a rectangular matrix and integers a and b, consider the union of the ath row and the bth (both 0-based)
column of the matrix (i.e. all cells that belong either to the ath row or to the bth column, or to both).
Return sum of all elements of that union.

Example

For

matrix = [[1, 1, 1, 1],
          [2, 2, 2, 2],
          [3, 3, 3, 3]]
a = 1, and b = 3, the output should be
solution(matrix, a, b) = 12.

Here (2 + 2 + 2 + 2) + (1 + 3) = 12.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer matrix

2-dimensional array of integers representing a rectangular matrix.

Guaranteed constraints:
1 ≤ matrix.length ≤ 500,
1 ≤ matrix[0].length ≤ 500,
1 ≤ matrix[i][j] ≤ 105.

[input] integer a

A non-negative integer less than the number of matrix rows.

Guaranteed constraints:
0 ≤ a < matrix.length.

[input] integer b

A non-negative integer less than the number of matrix columns.

Guaranteed constraints:
0 ≤ b < matrix[i].length.

[output] integer
'''
def f(m, a, b):
    return sum(m[a]) + sum(m[i][b] for i in range(len(m))) - m[a][b]
