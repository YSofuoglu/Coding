'''
Some people run along a straight line in the same direction. They start
simultaneously at pairwise distinct positions and run with constant speed
(which may differ from person to person).

If two or more people are at the same point at some moment we call that a
meeting. The number of people gathered at the same point is called meeting
cardinality.

For the given starting positions and speeds of runners find the maximum meeting
cardinality assuming that people run infinitely long. If there will be no
meetings, return -1 instead.

Example

For startPosition = [1, 4, 2] and speed = [27, 18, 24], the output should be
solution(startPosition, speed) = 3.

In 20 seconds after the runners start running, they end up at the same point.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer startPosition

A non-empty array of integers representing starting positions of runners
(in meters).

Guaranteed constraints:
2 ≤ startPosition.length ≤ 100,
-104 ≤ startPosition[i] ≤ 104.

[input] array.integer speed

Array of positive integers of the same length as startPosition representing
speeds of the runners (in meters per minute).

Guaranteed constraints:
speed.length = startPosition.length,
1 ≤ speed[i] ≤ 100.

[output] integer

The maximum meeting cardinality or -1 if there will be no meetings.
'''
def f(x0, v):
    max_meets = -1
    for i in range(len(x0)):
        for j in range(i + 1, len(x0)):
            if v[j] != v[i]:
                t = (x0[i] - x0[j]) / (v[j] - v[i])
                if t >= 0:
                    meet = 2
                    for k in range(j + 1, len(x0)):
                        if (x0[i] + v[i] * t ==
                            x0[k] + v[k] * t):
                            meet += 1
                    if meet > max_meets:
                        max_meets = meet
    return max_meets
