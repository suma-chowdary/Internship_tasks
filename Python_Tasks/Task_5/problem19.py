
# Problem: Merge the Tools!
# HackerRank: https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        part = string[i:i + k]
        result = ''.join(dict.fromkeys(part))
        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
