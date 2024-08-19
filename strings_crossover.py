'''Define crossover operation over two equal-length strings A and B as follows:

the result of that operation is a string of the same length as the input strings
result[i] is either A[i] or B[i], chosen at random
Given array of strings inputArray and a string result, find for how many pairs of strings 
from inputArray the result of the crossover operation over them may be equal to result.

Note that (A, B) and (B, A) are the same pair. Also note that the pair cannot include the 
same element of the array twice (however, if there are two equal elements in the array, 
they can form a pair).

Example

For inputArray = ["abc", "aaa", "aba", "bab"] and result = "bbb", the output should be
solution(inputArray, result) = 2.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.string inputArray

A non-empty array of equal-length strings.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
1 ≤ inputArray[i].length ≤ 10.

[input] string result

A string of the same length as each of the inputArray elements.

Guaranteed constraints:
result.length = inputArray[i].length.

[output] integer
'''

def f(a, r):
    count = 0
    while len(a) > 1:
        b = a[0]
        for c in a[1:]:
            if all((r[i] == b[i] or r[i] == c[i]) for i in range(len(r))):
                count += 1
        a.pop(0)
    return count
