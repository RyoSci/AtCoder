n, t = map(int, input().split())
a = 0
b = 0
a_b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a += ai
    b += bi
    a_b.append(ai - bi)

a_b.sort(reverse=True)

if a <= t:
    ans = 0
elif b > t:
    ans = -1
else:
    for i in range(n):
        a -= a_b[i]
        if a <= t:
            ans = i + 1
            break
print(ans)
