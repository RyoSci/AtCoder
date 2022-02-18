import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

s = input().strip()
res = 0
for i in s:
    if i == "1":
        res += 1

print(res)
