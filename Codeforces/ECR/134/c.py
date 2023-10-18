# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_left
import sys
def input(): return sys.stdin.readline().rstrip()


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    d_min = [0]*n
    d_max = [0]*n

    r = n-1
    for i in range(n-1, -1, -1):
        pos = bisect_left(b, a[i])
        d_min[i] = b[pos] - a[i]
        d_max[i] = b[r] - a[i]
        if pos == i:
            r = i-1

    print(*d_min)
    print(*d_max)
