#!/bin/python3
# https://www.hackerrank.com/challenges/the-birthday-bar/problem?h_r=next-challenge&h_v=zen&isFullScreen=true

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#


def birthday(s: list, d: int, m: int):
    # Write your code here
    count = 0
    window = m
    fp = 0
    lp = fp + window
    for i in range(len(s)):
        if lp <= len(s):
            if sum(s[fp:lp]) == d:
                count += 1
        fp += 1
        lp = fp + window
    return count


if __name__ == "__main__":
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)
    print(result)
