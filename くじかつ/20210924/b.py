import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
res = []
while n > 0:
    if n % 2 == 0:
        res.append("B")
        n //= 2
    else:
        res.append("A")
        n -= 1

res = res[::-1]
print(*res, sep="")
