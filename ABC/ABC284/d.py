# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

m = 4*10**6
primes = [1]*m
primes[0] = 0
primes[1] = 0
for i in range(m):
    if primes[i] == 0:
        continue
    for j in range(i*2, m, i):
        primes[j] = 0

t = int(input())
for i in range(t):
    n = int(input())
    cnt = dict()
    for j in range(m):
        if primes[j] == 1:
            if n % j == 0:
                n //= j
                if j not in cnt:
                    cnt[j] = 0
                cnt[j] += 1
            if n % j == 0:
                n //= j
                cnt[j] += 1
    if n != 1:
        nn = int(n**(1/2))
        if n % nn == 0:
            cnt[nn] = 0
            cnt[nn] += 2
        else:
            if n not in cnt:
                cnt[n] = 0
            cnt[n] += 1

    ans = []
    for key, val in cnt.items():
        ans.append([val, key])

    ans.sort(reverse=True)
    print(ans[0][1], ans[1][1])
