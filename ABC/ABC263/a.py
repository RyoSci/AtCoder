# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

a = list(map(int, input().split()))
d = [0]*14

for i in a:
    d[i] += 1

s = False
t = False

for i in range(1, 14):
    if d[i] == 3:
        s = True
    if d[i] == 2:
        t = True

if s and t:
    print("Yes")
else:
    print("No")
