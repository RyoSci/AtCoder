import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

s = input().strip()
k = int(input())

for i in range(len(s)):
    if s[i] != "1":
        index = i
        num = s[i]
        break
else:
    print(1)
    exit()

if k <= index:
    print(1)
else:
    print(num)
