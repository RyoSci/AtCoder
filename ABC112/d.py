n, m = map(int, input().split())

for i in range(1, int(m ** 0.5) + 1):
    if m % i == 0:
        a = m // i
        if m // a >= n:
            ans = a
            break
        if m // i >= n:
            ans = i

print(ans)
