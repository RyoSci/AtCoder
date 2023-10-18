# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18


s = input()
t = input()

s = s+"_"

for i, ti in enumerate(t):
    if ti != s[i]:
        print(i+1)
        break
