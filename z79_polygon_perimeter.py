'''
You have a rectangular white board with some black cells. The black cells create a connected black figure, i.e. it is
possible to get from any black cell to any other one through connected adjacent (sharing a common side) black cells.

Find the perimeter of the black figure assuming that a single cell has unit length.

It's guaranteed that there is at least one black cell on the table.

Example

For

matrix = [[false, true,  true ],
          [true,  true,  false],
          [true,  false, false]]
the output should be
solution(matrix) = 12.



For

matrix = [[true, true,  true],
          [true, false, true],
          [true, true,  true]]
the output should be
solution(matrix) = 16.



Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.boolean matrix

A matrix of booleans representing the rectangular board where true means a black cell and false means a white one.

Guaranteed constraints:
2 ≤ matrix.length ≤ 5,
2 ≤ matrix[0].length ≤ 5.

[output] integer
'''
def f(m):
    r, c = len(m), len(m[0]) #rows and columns
    n = [(-1,0), (1,0), (0,-1), (0,1)] #neighbors
    return sum([4-sum(0 <= i + k < r and 0 <= j + l < c and m[i + k][j + l] for k, l in n)
    if m[i][j] else 0 for j in range(c) for i in range(r)])
