n, a, b = map(int, input().split())
s = [int(input()) for _ in range(n)]

if max(s) - min(s) == 0:
    ans = [-1]
else:
    p = b / (max(s) - min(s))
    q = a - sum(s) / n * p
    ans = [p, q]

print(*ans)
