#!/bin/python3

import os


def breakingRecords(scores):
    # Write your code here
    min_count, max_count, minimum, maximum = 0, 0, scores[0], scores[0]

    for score in scores:
        if score > maximum:
            maximum = score
            max_count += 1
        if score < minimum:
            minimum = score
            min_count += 1

    print(min_count, max_count)
    return max_count, min_count


if __name__ == "__main__":
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)
