# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

y = int(input())
for i in range(2000, 3010):
    if i % 4 == 2 and i >= y:
        print(i)
        break
