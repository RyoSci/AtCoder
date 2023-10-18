# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())

ans = []
while n > 0:
    if n % 2 == 1:
        ans.append("A")
        n -= 1
    else:
        ans.append("B")
        n //= 2

print("".join(ans[::-1]))
