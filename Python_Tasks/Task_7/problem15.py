
# Problem: Game of Thrones - I
# Link: https://www.hackerrank.com/challenges/game-of-thrones/problem

from collections import Counter

def gameOfThrones(s):
    counts = Counter(s)

    odd_count = 0

    for count in counts.values():
        if count % 2 != 0:
            odd_count += 1

    if odd_count <= 1:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    s = input().strip()
    print(gameOfThrones(s))
