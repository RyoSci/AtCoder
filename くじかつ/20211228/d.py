import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a, b = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


g = gcd(a, b)
now = g
ans = set()
for i in range(2, g+1):
    if i*i > g:
        break
    while 1:
        if now % i == 0:
            ans.add(i)
            # ans.add(now//i)
            now //= i
        else:
            break
if now != 1:
    ans.add(now)

print(len(ans)+1)
