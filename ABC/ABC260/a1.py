# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

"最初に実装しかけてやめた方針"

s = input()
d = dict()
for i in s:
    if i not in d:
        d[i] = 0
    d[i] += 1

for key, val in d.items():
    if val == 1:
        print(key)
        exit()
else:
    print(-1)
