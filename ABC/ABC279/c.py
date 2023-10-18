# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h, w = map(int, input().split())
s = []
for i in range(h):
    si = input()
    s.append(si)

t = []
for i in range(h):
    ti = input()
    t.append(ti)

ss = []
tt = []

for j in range(w):
    tmp = []
    for i in range(h):
        if s[i][j] == "#":
            tmp.append(1)
        else:
            tmp.append(0)
    ss.append(tuple(tmp))

    tmp = []
    for i in range(h):
        if t[i][j] == "#":
            tmp.append(1)
        else:
            tmp.append(0)
    tt.append(tuple(tmp))


ss.sort()
tt.sort()

if ss == tt:
    print("Yes")
else:
    print("No")
