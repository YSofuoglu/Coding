'''
Given a rectangular matrix of integers, check if it is possible to rearrange its rows in such a way that all its columns
become strictly increasing sequences (read from top to bottom).

Example

For

matrix = [[2, 7, 1],
          [0, 2, 0],
          [1, 3, 1]]
the output should be
solution(matrix) = false;

For

matrix = [[6, 4],
          [2, 2],
          [4, 3]]
the output should be
solution(matrix) = true.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer matrix

A 2-dimensional array of integers.

Guaranteed constraints:
1 ≤ matrix.length ≤ 10,
1 ≤ matrix[0].length ≤ 10,
-300 ≤ matrix[i][j] ≤ 300.

[output] boolean
'''
import itertools
def f(m):
    return any(all(s[i][j]<s[i+1][j] for i in range(len(s)-1) for j in range(len(s[0]))) for s in itertools.permutations(m))
