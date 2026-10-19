
# Problem: Caesar Cipher
# Link: https://www.hackerrank.com/challenges/caesar-cipher-1/problem

def caesarCipher(s, k):
    result = ""
    k = k % 26

    for ch in s:
        if ch.islower():
            result += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
        elif ch.isupper():
            result += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
        else:
            result += ch

    return result


if __name__ == '__main__':
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())

    print(caesarCipher(s, k))
