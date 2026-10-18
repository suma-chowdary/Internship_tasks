
# Problem: Company Logo (Most Commons)
# HackerRank: https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter

if __name__ == '__main__':
    s = input()

    counts = Counter(s)
    result = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    for char, count in result[:3]:
        print(char, count)
