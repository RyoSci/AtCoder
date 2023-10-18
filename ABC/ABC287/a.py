# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
cnt = 0
for i in range(n):
    s = input()
    if s == "For":
        cnt += 1

if cnt > n//2:
    print("Yes")
else:
    print("No")
