
# Problem: Funny String
# Link: https://www.hackerrank.com/challenges/funny-string/problem

def funnyString(s):
    reverse_s = s[::-1]

    for i in range(1, len(s)):
        original_diff = abs(ord(s[i]) - ord(s[i - 1]))
        reverse_diff = abs(ord(reverse_s[i]) - ord(reverse_s[i - 1]))

        if original_diff != reverse_diff:
            return "Not Funny"

    return "Funny"


if __name__ == '__main__':
    q = int(input().strip())

    for _ in range(q):
        s = input().strip()
        print(funnyString(s))
