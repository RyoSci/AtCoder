# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = 10**18


n = int(input())
seen = [0]*(2*n+1)
now = 0
while 1:

    while seen[now] == 1:
        now += 1
        now %= (2*n+1)

    print(now+1, flush=True)
    # sys.stdout.flush()
    seen[now] = 1

    nn = int(input())
    if nn == 0:
        exit()
    seen[nn-1] = 1
