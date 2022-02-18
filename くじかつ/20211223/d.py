import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

ans = 0
for i in range(1, n+1):
    if i*i > n:
        break
    ans += n / i + (n / i - n / (i + 1)) * i
    if i * i == n:
        ans -= i

print(ans)
