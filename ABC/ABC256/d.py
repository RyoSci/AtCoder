# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18
n = int(input())
m = 2*10**5+10
g = [0]*m
for i in range(n):
    l, r = map(int, input().split())
    g[l] += 1
    g[r] -= 1

for i in range(m-1):
    g[i+1] += g[i]

ans = []
l = 0
r = 0
flag = False
for i in range(1, m):
    if g[i] > 0:
        if not flag:
            l = i
        flag = True
        r = i
    else:
        if flag:
            ans.append([l, r])
        flag = False

for x, y in ans:
    print(x, y+1)

# print(g[:60])
# print(ans[:60])
