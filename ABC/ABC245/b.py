# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = set(map(int, input().split()))

now = 0
while 1:
    if now not in a:
        print(now)
        exit()
    now += 1
