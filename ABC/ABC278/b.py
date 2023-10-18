# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h, m = map(int, input().split())
hm = h*60+m

while 1:
    h = hm//60 % 24
    m = hm % 60
    h = str(h).zfill(2)
    m = str(m).zfill(2)

    nh = h[0] + m[0]
    nm = h[1]+m[1]

    nh = int(nh)
    nm = int(nm)
    if 0 <= nh <= 23 and 0 <= nm <= 59:
        print(int(h), int(m))
        exit()

    hm += 1
