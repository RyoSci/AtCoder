# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = 10**18

n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    b.append([a[i], i])

b.sort()

print(b[-2][1]+1)
