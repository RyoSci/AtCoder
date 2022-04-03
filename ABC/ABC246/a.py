# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

x = []
y = []
xd = dict()
yd = dict()
for i in range(3):
    xi, yi = map(int, input().split())
    if xi not in xd:
        xd[xi] = 0
    xd[xi] += 1
    if yi not in yd:
        yd[yi] = 0
    yd[yi] += 1

ansx = -1
for key, val in xd.items():
    if val == 1:
        ansx = key
ansy = -1
for key, val in yd.items():
    if val == 1:
        ansy = key
print(ansx, ansy)
