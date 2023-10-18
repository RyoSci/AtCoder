# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

k = int(input())

ele = dict()
now = k
for i in range(2, k):
    if i*i > k:
        break

    while now % i == 0:
        if i not in ele:
            ele[i] = 0
        ele[i] += 1
        now //= i

if now != 1:
    if now not in ele:
        ele[now] = 0
    ele[now] += 1

ans = 0
for key, val in ele.items():
    cnt = 0
    for i in range(1, 42):
        now = key*i
        while now % key == 0:
            now //= key
            cnt += 1
        if cnt >= val:
            ans = max(ans, key*i)
            break
print(ans)
