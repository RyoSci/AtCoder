import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, X = map(int, input().split())
x = list(map(int, input().split()))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


d = abs(x[0]-X)
for i in range(1, n):
    d = gcd(d, abs(x[i]-X))

print(d)
