
# Problem: Alternating Characters
# Link: https://www.hackerrank.com/challenges/alternating-characters/problem

def alternatingCharacters(s):
    count = 0

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1

    return count


if __name__ == '__main__':
    q = int(input().strip())

    for _ in range(q):
        s = input().strip()
        print(alternatingCharacters(s))
