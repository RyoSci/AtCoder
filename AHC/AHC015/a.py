# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

a = list(map(int, input().split()))
cnt = [0]*3

for i in range(100):
    cnt[a[i]-1] += 1

tmp = []
for i in range(3):
    tmp.append((cnt[i], i))

tmp.sort()
most = tmp[-1][-1]

for i in range(100):
    if a[i] == most:
        print("B", flush=True)
    else:
        print("L", flush=True)

    t = int(input())
