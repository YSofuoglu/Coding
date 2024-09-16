'''In ChessLand there is a small but proud chess bishop with a recurring dream. In the dream the bishop finds itself on an
n × m chessboard with mirrors along each edge, and it is not a bishop but a ray of light. This ray of light moves only along
diagonals (the bishop can't imagine any other types of moves even in its dreams), it never stops, and once it reaches an
edge or a corner of the chessboard it reflects from it and moves on.

Given the initial position and the direction of the ray, find its position after k steps where a step means either moving
from one cell to the neighboring one or reflecting from a corner of the board.

Example

For boardSize = [3, 7], initPosition = [1, 2],
initDirection = [-1, 1], and k = 13, the output should be
solution(boardSize, initPosition, initDirection, k) = [0, 1].

Here is the bishop's path:

[1, 2] -> [0, 3] -(reflection from the top edge)-> [0, 4] ->
[1, 5] -> [2, 6] -(reflection from the bottom right corner)-> [2, 6] ->
[1, 5] -> [0, 4] -(reflection from the top edge)-> [0, 3] ->
[1, 2] -> [2, 1] -(reflection from the bottom edge)-> [2, 0] -(reflection from the left edge)->
[1, 0] -> [0, 1]


Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer boardSize

An array of two integers, the number of rows and columns, respectively. Rows are numbered by integers from 0 to
boardSize[0] - 1, columns are numbered by integers from 0 to boardSize[1] - 1 (both inclusive).

Guaranteed constraints:
1 ≤ boardSize[i] ≤ 20.

[input] array.integer initPosition

An array of two integers, indices of the row and the column where the bishop initially stands, respectively.

Guaranteed constraints:
0 ≤ initPosition[i] < boardSize[i].

[input] array.integer initDirection

An array of two integers representing the initial direction of the bishop. If it stands in (a, b), the next cell he'll move
to is (a + initDirection[0], b + initDirection[1]) or whichever it'll reflect to in case it runs into a mirror immediately.

Guaranteed constraints:
initDirection[i] ∈ {-1, 1}.

[input] integer k

Guaranteed constraints:
1 ≤ k ≤ 109.

[output] array.integer

The position of the bishop after k steps.'''
def f(s, iP, iD, k):#s:boardSize, iP:initPosition, iD:initDirection
    vs = (iP[0] if iD[0] == 1 else s[0]-iP[0]-1) + k #vertical steps
    hs = (iP[1] if iD[1] == 1 else s[1]-iP[1]-1) + k #horizontal steps
    p = [vs % s[0], hs % s[1]] # last position
    if (vs // s[0] + (iD[0] == -1)) % 2: p[0] = s[0]-p[0]-1
    if (hs // s[1] + (iD[1] == -1)) % 2: p[1] = s[1]-p[1]-1
    return p
