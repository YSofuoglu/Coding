'''Consider a bishop, a knight and a rook on an n × m chessboard. They are said to form a triangle if each piece attacks
exactly one other piece and is attacked by exactly one piece. Calculate the number of ways to choose positions of the pieces
to form a triangle.

Note that the bishop attacks pieces sharing the common diagonal with it; the rook attacks in horizontal and vertical
directions; and, finally, the knight attacks squares which are two squares horizontally and one square vertically, or two
squares vertically and one square horizontally away from its position.

Example

For n = 2 and m = 3, the output should be
solution(n, m) = 8.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 40.

[input] integer m

Guaranteed constraints:
1 ≤ m ≤ 40,
3 ≤ n · m.

[output] integer'''
def f(n, m):
    return sum((ways(n, m, x, y) + ways(m, n, x, y)) * 8 for x, y in [(2, 3), (3, 3), (2, 4), (3, 4)])

def ways(n, m, x, y):
    return (n - x + 1) * (m - y + 1) if n >= x and m >= y else 0
