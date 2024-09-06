'''
In the Land Of Chess, bishops don't really like each other. In fact, when two bishops happen to stand on the same diagonal,
they immediately rush towards the opposite ends of that same diagonal.

Given the initial positions (in chess notation) of two bishops, bishop1 and bishop2, calculate their future positions. Keep
in mind that bishops won't move unless they see each other along the same diagonal.

Example

For bishop1 = "d7" and bishop2 = "f5", the output should be
solution(bishop1, bishop2) = ["c8", "h3"].

For bishop1 = "d8" and bishop2 = "b5", the output should be
solution(bishop1, bishop2) = ["b5", "d8"].

The bishops don't belong to the same diagonal, so they don't move.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string bishop1

Coordinates of the first bishop in chess notation.

Guaranteed constraints:
bishop1.length = 2,
'a' ≤ bishop1[0] ≤ 'h',
1 ≤ bishop1[1] ≤ 8.

[input] string bishop2

Coordinates of the second bishop in the same notation.

Guaranteed constraints:
bishop2.length = 2,
'a' ≤ bishop2[0] ≤ 'h',
1 ≤ bishop2[1] ≤ 8.

[output] array.string

Coordinates of the bishops in lexicographical order after they check the diagonals they stand on.
'''
def f(b1, b2):
    c2n = lambda b: (ord(b[0]) - 96, int(b[1]))
    n2c = lambda x, y: chr(x + 96) + str(y)
    x1, y1 = c2n(b1)
    x2, y2 = c2n(b2)

    if abs(x1 - x2) == abs(y1 - y2):
        dx, dy = (1 if x1 < x2 else -1), (1 if y1 < y2 else -1)
        while 1 <= x1 - dx <= 8 and 1 <= y1 - dy <= 8: x1, y1 = x1 - dx, y1 - dy
        while 1 <= x2 + dx <= 8 and 1 <= y2 + dy <= 8: x2, y2 = x2 + dx, y2 + dy
        return sorted([n2c(x1, y1), n2c(x2, y2)])

    return sorted([b1, b2])
