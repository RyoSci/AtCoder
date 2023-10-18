# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))
# n = 2*10**5
# a = [10**8+i for i in range(n)]


d = dict()
for i in range(n):
    if a[i] not in d:
        d[a[i]] = 0
    d[a[i]] += 1

keys = list(d.keys())
keys.sort(reverse=True)

ans = [0]*n
for i, key in enumerate(keys):
    ans[i] = d[key]

print(*ans, sep="\n")
