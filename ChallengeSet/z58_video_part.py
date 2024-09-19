'''You have been watching a video for some time. Knowing the total video duration find out what portion of the video you have
already watched.

Example

For part = "02:20:00" and total = "07:00:00", the output should be
solution(part, total) = [1, 3].

You have watched 1 / 3 of the whole video.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string part

A string of the following format "hh:mm:ss" representing the time you have been watching the video.

[input] string total

A string of the following format "hh:mm:ss" representing the total video duration.

[output] array.integer

An array of the following format [a, b] (where a / b is a reduced fraction).'''
def f(part, total):
    p = part.split(":")
    t = total.split(":")
    x = lambda x: int(x[0])*3600 + int(x[1])*60 + int(x[2])
    from fractions import Fraction
    y = Fraction(x(p),x(t))
    return [y.numerator, y.denominator]
