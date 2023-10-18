# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = input()

st = [[] for _ in range(n+1)]
lcnt = 0
for i in range(n):
    if s[i] == "(":
        lcnt += 1
        st[lcnt].append(s[i])
    elif s[i] == ")":
        if lcnt == 0:
            st[lcnt].append(s[i])
        else:
            st[lcnt] = []
            lcnt -= 1
    else:
        st[lcnt].append(s[i])

ans = ""
for i in range(n+1):
    ans += "".join(st[i])

print(ans)
