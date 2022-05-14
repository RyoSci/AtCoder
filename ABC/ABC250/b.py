# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, a, b = list(map(int, input().split()))

ans = []
for i in range(n*a):
    line = ""
    for j in range(n*b):
        if (i//a+j//b) % 2 == 0:
            line += "."
        else:
            line += "#"
    ans.append(line)
for i in ans:
    print(i)
