import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

s, t = map(int, input().split())

res = 0
for a in range(101):
    for b in range(101):
        for c in range(101):
            if a+b+c <= s and a*b*c <= t:
                res += 1

print(res)
