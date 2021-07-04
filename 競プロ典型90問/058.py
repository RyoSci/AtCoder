n, k = map(int, input().split())
memo = [-1] * 10**5


def f(z):
    tmp = 0
    for i in range(6):
        tmp += z % 10
        z //= 10
    return tmp


z = n
mod = 10**5
cnt = 0
for i in range(10**6):
    if memo[z] == -1:
        memo[z] = cnt
    else:
        cycle = cnt-memo[z]
        break
    z = z+f(z)
    z %= mod
    cnt += 1

if k > 10**5:
    k = (k-memo[z]) % cycle
else:
    z = n

for i in range(k):
    z = z+f(z)
    z %= mod

print(z)
