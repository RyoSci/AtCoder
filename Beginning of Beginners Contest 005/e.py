import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

q = int(input())
tx = [list(map(int, input().split())) for _ in range(q)]

d = dict()
for i in range(q):
    t, x = tx[i]
    if t == 1:
        if x not in d:
            d[x] = 0
        d[x] += 1

keys = sorted(list(d.keys()), reverse=True)
now = 0

ans = []
for i in range(q):
    t, x = tx[i]
    if t == 0:
        while 1:
            if d[keys[now]] > 0:
                ans.append(keys[now])
                break
            else:
                now += 1
    else:
        d[x] -= 1

print(*ans, sep="\n")
