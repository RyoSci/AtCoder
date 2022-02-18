import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, q = map(int, input().split())
a = list(map(int, input().split()))

cnt = dict()
res = dict()

for i in range(n):
    if a[i] not in cnt:
        cnt[a[i]] = 0
    cnt[a[i]] += 1
    res[(a[i], cnt[a[i]])] = i+1

ans = []
for i in range(q):
    x, k = map(int, input().split())
    if (x, k) not in res:
        ans.append(-1)
    else:
        ans.append(res[(x, k)])

print(*ans, sep="\n")
