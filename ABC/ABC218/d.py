import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

ys = dict()

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if y not in ys:
        ys[y] = set()
    ys[y].add(x)

ys_keys = sorted(list(ys.keys()))
m = len(ys_keys)

res = 0
for i in range(m-1):
    for j in range(i+1, m):
        tmp = len(ys[ys_keys[i]] & ys[ys_keys[j]])
        res += tmp*(tmp-1)//2

print(res)
