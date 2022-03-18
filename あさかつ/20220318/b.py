# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = 10**18

n, m, a, b = list(map(int, input().split()))

for i in range(m):
    if n <= a:
        n += b
    c = int(input())
    n -= c
    if n < 0:
        print(i+1)
        exit()
else:
    print("complete")
