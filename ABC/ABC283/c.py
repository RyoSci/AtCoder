# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = input()
n = len(s)
z = []
now = 0
ans = 0
for i in range(n):
    if s[i] == '0':
        now += 1
    else:
        z.append(now)
        now = 0
        ans += 1

if now > 0:
    z.append(now)
    now = 0

for i in z:
    ans += (i+1)//2

print(ans)
