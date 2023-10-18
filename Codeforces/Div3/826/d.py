# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from math import log2
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


t = int(input())
for _ in range(t):
    m = int(input())
    p = list(map(int, input().split()))
    h = int(log2(m))

    ans = 0
    for i in range(h, 0, -1):
        tmp = []
        for j in range(0, m, 2):
            l = (p[j]+1)//2
            r = (p[j+1]+1)//2
            if l == r:
                tmp.append(l)
                if p[j] > p[j+1]:
                    ans += 1
            else:
                ans = -1
                break
        m //= 2
        p = tmp
        if ans == -1:
            break
    print(ans)
