# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = []
for i in range(10):
    si = input()
    s.append(si)

ans = []
for i in range(10):
    for j in range(10):
        if s[i][j] == "#":
            ans.append((i+1, j+1))

ans.sort()
a = ans[0][0]
b = ans[-1][0]
c = ans[0][1]
d = ans[-1][1]

print(a, b)
print(c, d)
