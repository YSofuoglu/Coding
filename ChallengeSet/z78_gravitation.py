'''
You are given a vertical box divided into equal columns. Someone dropped several stones from its top through the columns.
Stones are falling straight down at a constant speed (equal for all stones) while possible (i.e. while they haven't reached
the ground or they are not blocked by another motionless stone). Given the state of the box at some moment in time, find
out which columns become motionless first.

Example

For

rows = ["#..##",
        ".##.#",
        ".#.##",
        "....."]
the output should be solution(rows) = [1, 4].

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.string rows

A non-empty array of strings of equal length consisting only of #-s and .-s describing the box at a specific moment in time.
Sharps represent stones, and dots represent empty cells. row[0] corresponds to the upper row. Last element of rows corresponds
to the ground level.

Guaranteed constraints:
2 ≤ rows.length ≤ 100,
2 ≤ rows[i].length ≤ 100.

[output] array.integer

A sorted array containing numbers of all columns (leftmost column's number is 0) in which movements will stop at the same
second and earlier than in any other column. Assume that if there are no stones in a column then movement stops immediately,
i.e. after 0 seconds.
'''
def f(m):
    c = []
    y = [[m[i][j]  for i in range(len(m))] for j in range(len(m[0]))]
    for s in y:
      if '#' not in s:
        c.append(0)
      else:
        c.append(s[s.index('#'):].count('.'))
    return sorted([i for i,x in enumerate(c) if x==min(c)])
