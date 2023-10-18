# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = input()

ans = 0
zo = [0]*2
for i in range(n):
    nxt = [0]*2
    if s[i] == "1":
        nxt[1] += 1
        nxt[1] += zo[0]
        nxt[0] += zo[1]
    else:
        nxt[0] += 1
        nxt[1] += zo[1]
        nxt[1] += zo[0]
    zo = nxt
    ans += zo[1]

print(ans)
