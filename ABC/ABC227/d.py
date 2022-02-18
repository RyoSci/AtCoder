import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
if k == 1:
    print(sum(a))
    exit()

t = [0]*(n+2)
for i in range(n):
    t[1] += 1
    t[min(a[i]+1, n+1)] -= 1

for i in range(n+1):
    t[i+1] += t[i]

for i in range(n+1):
    dis = t[i]-k
    if dis > 0:
        # t[i+1] += min(t[i]-t[i+1], dis)
        t[i+1] += min(dis, t[i]-t[i+1])
        t[i] -= dis
    # print(t, i)

res = 0
for i in range(n+2):
    if t[i] >= k:
        res += 1

print(res)
