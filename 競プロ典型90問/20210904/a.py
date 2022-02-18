import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

d = dict()
for i in range(2, int(n**0.5)+1):
    while n > 1:
        if n % i == 0:
            if i not in d:
                d[i] = 0
            d[i] += 1
            n //= i
        else:
            break

if n > 1:
    if n not in d:
        d[n] = 0
    d[n] += 1

cnt = 0
for val in d.values():
    cnt += val


for i in range(100):
    if 2**i >= cnt:
        break
print(i)
