n = int(input())
s = list(input())
q = int(input())
cnt = 0
for i in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        if cnt == 0:
            s[a - 1], s[b - 1] = s[b - 1], s[a - 1]
        else:
            a = (a + n) % (2 * n)
            b = (b + n) % (2 * n)
            s[a - 1], s[b - 1] = s[b - 1], s[a - 1]

    else:
        cnt ^= 1


if cnt == 1:
    s = s[n:] + s[:n]

print("".join(s))
