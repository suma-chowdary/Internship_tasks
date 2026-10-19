
# Problem: Anagram
# Link: https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter

def anagram(s):
    n = len(s)

    if n % 2 != 0:
        return -1

    first = s[:n // 2]
    second = s[n // 2:]

    count1 = Counter(first)
    count2 = Counter(second)

    changes = 0

    for ch in count1:
        if count1[ch] > count2[ch]:
            changes += count1[ch] - count2[ch]

    return changes


if __name__ == '__main__':
    q = int(input().strip())

    for _ in range(q):
        s = input().strip()
        print(anagram(s))
