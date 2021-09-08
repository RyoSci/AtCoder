import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

q = int(input())

primes = [1]*(10**5+1)
primes[0], primes[1] = 0, 0

for i in range(2, 10**5+1):
    if primes[i] == 0:
        continue
    for j in range(2*i, 10**5+1, i):
        primes[j] = 0

like_2017 = [0]*(10**5+2)
for i in range(10**5+1):
    if primes[i] and primes[(i+1)//2]:
        like_2017[i] = 1

s_like = [0]*(10**5+2)
for i in range(10**5+1):
    s_like[i] = s_like[i-1]+like_2017[i]

for i in range(q):
    l, r = map(int, input().split())
    print(s_like[r]-s_like[l-1])
