# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, q = map(int, input().split())
s = input()
top = 0
ans = []
for i in range(q):
    num, x = map(int, input().split())
    if num == 1:
        top -= x
        top %= n
    else:
        ans.append(s[(top+x-1) % n])

print(*ans)
