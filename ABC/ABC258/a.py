# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
input=lambda: sys.stdin.readline().rstrip()
INF = 10**18

k = int(input())
h = str(21+k//60)
m = str(k%60)
print(h+":"+m.zfill(2))