# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

x, y, z, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = []
for i in range(x):
    for j in range(y):
        ans.append(a[i]+b[j])

ans.sort(reverse=True)
tmp = min(k, len(ans))
ans = ans[:tmp]

ans2 = []
for i in range(tmp):
    for j in range(z):
        ans2.append(ans[i]+c[j])

ans2.sort(reverse=True)

print(*ans2[:k], sep="\n")
