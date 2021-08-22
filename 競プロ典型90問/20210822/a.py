n, q = map(int, input().split())
a = list(map(int, input().split()))

start = 0
ans = []
for i in range(q):
    t, x, y = map(int, input().split())
    x -= 1
    y -= 1
    if t == 1:
        a[(start+x) % n], a[(start+y) % n] = a[(start+y) % n], a[(start+x) % n]
    elif t == 2:
        start -= 1
        start %= n
    else:
        ans.append(a[(start+x) % n])

print(*ans, sep="\n")
