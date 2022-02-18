import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
pins = [1]*(m+1)
pins[0] = 0

res = 0
for i in range(1, n+1):
    a, b = map(int, input().split())
    tmp = i-(a+b)
    if 1 <= tmp <= m and pins[tmp] == 1:
        res += 1
        pins[tmp] = 0

print(res)
