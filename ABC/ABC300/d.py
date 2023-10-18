# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
m = 10**6
primes = [1] * m
primes[0] = 0
primes[1] = 0
for i in range(2, m):
    for j in range(i+i, m, i):
        primes[j] = 0

bs = []
for i in range(10**4):
    if primes[i]:
        bs.append(i)

for i in range(m-1):
    primes[i+1] += primes[i]

ans = 0
for b in bs:
    for a in bs:
        if a >= b:
            break
        if a*a*b > n:
            break

        c2 = n/(a*a*b)
        c = c2**(0.5)
        c = int(c)

        if b < c:
            ans += primes[c]-primes[b]
        else:
            break


print(ans)
