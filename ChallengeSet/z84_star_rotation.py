'''
Consider a (2k+1) × (2k+1) square subarray of an integer integers matrix. Let's call the union of the square's
two longest diagonals, middle column and middle row a star. Given the coordinates of the star's center in the
matrix and its width, rotate it 45 · t degrees clockwise preserving position of all matrix elements that do not
belong to the star.

Example

For

matrix = [[1, 0, 0, 2, 0, 0, 3],
          [0, 1, 0, 2, 0, 3, 0],
          [0, 0, 1, 2, 3, 0, 0],
          [8, 8, 8, 9, 4, 4, 4],
          [0, 0, 7, 6, 5, 0, 0],
          [0, 7, 0, 6, 0, 5, 0],
          [7, 0, 0, 6, 0, 0, 5]]
width = 7, center = [3, 3], and t = 1, the output should be

solution(matrix, width, center, t) = [[8, 0, 0, 1, 0, 0, 2],
                                          [0, 8, 0, 1, 0, 2, 0],
                                          [0, 0, 8, 1, 2, 0, 0],
                                          [7, 7, 7, 9, 3, 3, 3],
                                          [0, 0, 6, 5, 4, 0, 0],
                                          [0, 6, 0, 5, 0, 4, 0],
                                          [6, 0, 0, 5, 0, 0, 4]]
For

matrix = [[1, 0, 0, 2, 0, 0, 3],
          [0, 1, 0, 2, 0, 3, 0],
          [0, 0, 1, 2, 3, 0, 0],
          [8, 8, 8, 9, 4, 4, 4],
          [0, 0, 7, 6, 5, 0, 0]]
width = 3, center = [1, 5], and t = 81, the output should be

solution(matrix, width, center, t) = [[1, 0, 0, 2, 0, 0, 0],
                                          [0, 1, 0, 2, 3, 3, 3],
                                          [0, 0, 1, 2, 0, 0, 0],
                                          [8, 8, 8, 9, 4, 4, 4],
                                          [0, 0, 7, 6, 5, 0, 0]]
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer matrix

A two-dimensional array of integers.

Guaranteed constraints:
3 ≤ matrix.length ≤ 15,
3 ≤ matrix[i].length ≤ 15,
matrix[i].length == matrix[j].length,
0 ≤ matrix[i][j] ≤ 99.

[input] integer width

An odd integer representing the star's width. It equals the length of the sides of the bounding square for the star.

Guaranteed constraints:
3 ≤ width ≤ min(matrix.length, matrix[i].length).

[input] array.integer center

An array of two integers.

Guaranteed constraints:
center.length = 2,
(width - 1) / 2 ≤ center[0] < matrix.length - (width - 1) / 2,
(width - 1) / 2 ≤ center[1] < matrix[i].length - (width - 1) / 2.

[input] integer t

A non-negative integer denoting how many times the star should be rotated by 45 degrees.

Guaranteed constraints:
0 ≤ t ≤ 109.

[output] array.array.integer

An array with specified star rotated by 45 · t degrees.
'''
def f(m, w, c, t):
    x, y = c[0], c[1]
    for i in range(t%8):
        for j in range(1,(w-1)//2+1):
            m[x-j][y], m[x-j][y+j], m[x][y+j], m[x+j][y+j], m[x+j][y], m[x+j][y-j], m[x][y-j], m[x-j][y-j]
            = m[x-j][y-j], m[x-j][y], m[x-j][y+j], m[x][y+j], m[x+j][y+j], m[x+j][y], m[x+j][y-j], m[x][y-j]
    return m
