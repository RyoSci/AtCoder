n, k = map(int, input().split())
a = list(map(int, input().split()))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


min_ball = a[0]
for i in range(n - 1):
    min_ball = gcd(min_ball, a[i + 1])

ans = "IMPOSSIBLE"
for i in range(n):
    if a[i] == k:
        ans = "POSSIBLE"
        break
    elif a[i] > k and (a[i] - k) % min_ball == 0:
        ans = "POSSIBLE"
        break

print(ans)
