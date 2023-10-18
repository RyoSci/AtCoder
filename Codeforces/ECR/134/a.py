# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

t = int(input())
for _ in range(t):
    g = [list(input()) for _ in range(2)]
    d = [0]*26
    for i in range(2):
        for j in range(2):
            d[ord(g[i][j])-ord("a")] += 1
    res = []
    for i in range(26):
        if d[i] > 0:
            res.append(d[i])
    res.sort()

    if res == [4]:
        print(0)
    if res == [1, 3]:
        print(1)
    if res == [2, 2]:
        print(1)
    if res == [1, 1, 2]:
        print(2)
    if res == [1, 1, 1, 1]:
        print(3)
