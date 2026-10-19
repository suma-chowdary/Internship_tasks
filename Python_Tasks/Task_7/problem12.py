
# Problem: Making Anagrams
# Link: https://www.hackerrank.com/challenges/making-anagrams/problem

from collections import Counter

def makingAnagrams(s1, s2):
    count1 = Counter(s1)
    count2 = Counter(s2)

    total = 0

    for ch in set(s1 + s2):
        total += abs(count1[ch] - count2[ch])

    return total


if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()

    print(makingAnagrams(s1, s2))
