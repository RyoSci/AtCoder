# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
m = 10**6 + 10
nums = [0]*m
for i in range(2, m):
    if nums[i] == 1:
        continue
    for j in range(2*i, m, i):
        nums[j] = 1

primes = []
for i in range(2, m):
    if nums[i] == 0:
        primes.append(i)

k = len(primes)
r = k-1
ans = 0
for l in range(k):
    if l >= r:
        break
    while l < r and primes[l]*primes[r]**3 > n:
        r -= 1
    if l < r:
        ans += r-l

print(ans)
