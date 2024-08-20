'''
You're given a substring s of some cyclic string. What's the length of the
smallest possible string that can be concatenated to itself many times to
obtain this cyclic string?

Example

For s = "cabca", the output should be
solution(s) = 3.

"cabca" is a substring of a cycle string "abcabcabcabc..." that can be obtained
by concatenating "abc" to itself. Thus, the answer is 3.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string s

Guaranteed constraints:
3 ≤ s.length ≤ 15.

[output] integer

[Python 3] Syntax Tips
'''
def f(s):
    return next((i + 1 for i in range(len(s)) if s in s[0:i+1] * (len(s) // (i+1) + 1)), 0)
