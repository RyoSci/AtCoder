# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = input()
w = list(map(int, input().split()))
ws = []

for i in range(n):
    ws.append((w[i], int(s[i])))

ws.sort()

ad = 0
for i in range(n):
    if s[i] == "1":
        ad += 1

ans = max(ad, n-ad)
ch = 0
for i in range(n-1):
    wi, si = ws[i]
    if si == 1:
        ad -= 1
    else:
        ch += 1
    if i != n-1 and wi != ws[i+1][0]:
        res = ad+ch
        ans = max(ans, res)

print(ans)
