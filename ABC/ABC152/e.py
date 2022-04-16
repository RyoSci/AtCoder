# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18
MOD = 10**9+7

n = int(input())
a = list(map(int, input().split()))


def div_element(x):
    n = x
    res = dict()
    for i in range(2, n+1):
        if i*i > n:
            break
        while 1:
            if x % i == 0:
                if i not in res:
                    res[i] = 0
                res[i] += 1
                x //= i
            else:
                break
    if x > 1:
        if x not in res:
            res[x] = 0
        res[x] += 1
    return res


m = 10**6
ele_max = [0]*m

for i in range(n):
    res = div_element(a[i])
    for key, val in res.items():
        ele_max[key] = max(ele_max[key], val)

x = 1
for i in range(m):
    if ele_max[i] > 0:
        x *= pow(i, ele_max[i], MOD)
        x %= MOD

ans = 0
for i in range(n):
    ans += x*pow(a[i], MOD-2, MOD)
    # ans += x//a[i]
    ans %= MOD

print(ans)
