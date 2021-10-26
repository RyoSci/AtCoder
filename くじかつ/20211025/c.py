import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
a = [0, n+1]+a
a.sort()

whites = []
stamp = n
for i in range(m+1):
    tmp = a[i+1]-a[i]-1
    if tmp == 0:
        continue
    stamp = min(stamp, tmp)
    whites.append(tmp)

res = 0
for i in whites:
    res += (i+stamp-1)//stamp

print(res)
