"""
You have a long strip of paper with integers written on it in a single line from left to right. 
You wish to cut the paper into exactly three pieces such that each piece contains at least one 
integer and the sum of the integers in each piece is the same. You cannot cut through a number, 
i.e. each initial number will unambiguously belong to one of the pieces after cutting. 
How many ways can you do it?

It is guaranteed that the sum of all elements in the array is divisible by 3.

Example

For a = [0, -1, 0, -1, 0, -1], the output should be
solution(a) = 4.

Here are all possible ways:

[0, -1] [0, -1] [0, -1]
[0, -1] [0, -1, 0] [-1]
[0, -1, 0] [-1, 0] [-1]
[0, -1, 0] [-1] [0, -1]
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer a

Guaranteed constraints:
5 ≤ a.length ≤ 104,
-108 ≤ a[i] ≤ 108.

[output] integer

It's guaranteed that for the given test cases the answer always fits signed 32-bit integer type.

SOLUTION:
The following code snippet seems quite decent, but due to its time complexity, it fails in almost half of the test cases.
"""

def f(a):
  return sum(sum(a[:i]) == sum(a[i:j]) == sum(a[j:]) for i in range(1, len(a)-1) for j in range(i + 1, len(a)))

"""So, the solution that passes all the test cases is as follows:"""

def f(a):
    total_sum = sum(a) // 3
    partitions = 0
    current_sum = 0
    first = 0

    for i in range(len(a) - 1):
        current_sum += a[i]
        if current_sum == total_sum :
            first += 1
        if current_sum == 2 * total_sum :
            partitions += first
            if total_sum  == 0:
                partitions -= 1

    return partitions
