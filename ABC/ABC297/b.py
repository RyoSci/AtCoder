# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = input()
n = len(s)

b = []
k = []
r = []
for i in range(n):
    if s[i] == "B":
        b.append(i)
    if s[i] == "K":
        k.append(i)
    if s[i] == "R":
        r.append(i)

ans = "No"
if(b[0] + b[1]) % 2 == 1:
    if r[0] <= k[0] <= r[1]:
        ans = "Yes"
print(ans)
