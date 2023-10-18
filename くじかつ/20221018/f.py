# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_left
import sys
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
b = [0]*(n+1)
for i in range(n):
    b[i+1] = b[i]+a[i]

cnt = [0]
tot = [0]

for i in range(1, n+1):
    cnt.append(cnt[-1]+i)
    if i % 2 == 1:
        tot.append(tot[-1]+(b[i]-b[0])*2)  # -a[(i+1)//2-1])
    else:
        tot.append(tot[-1]+(b[i]-b[0])*2)

for i in range(n-1, 0, -1):
    cnt.append(cnt[-1]+i)
    if i % 2 == 1:
        tot.append(tot[-1]+(b[n]-b[n-i])*2)  # -a[(n+n-i)//2-1])
    else:
        tot.append(tot[-1]+(b[n]-b[n-i])*2)


threshold = bisect_left(cnt, m)
ans = tot[threshold-1]
rest = m-cnt[threshold-1]

print(ans)
print(b)
print(cnt)
print(tot)

threshold = min(threshold, 2*n-threshold)
if threshold > n:
    threshold = threshold-n
    tmp = []
    for i in range(threshold, n):
        tmp.append(a[i]+a[n-1])
    tmp.sort(reverse=True)
    ans += sum(tmp[:rest])

else:
    tmp = []
    for i in range(threshold):
        tmp.append(a[i]+a[threshold-1-i])
    tmp.sort(reverse=True)
    ans += sum(tmp[:rest])

print(ans)

ans = 0
for i in range(n):
    for j in range(n):
        ans += a[i]+a[j]

print(ans)
