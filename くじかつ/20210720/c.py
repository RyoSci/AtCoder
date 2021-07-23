n = int(input())
s = list(input())
q = int(input())

flag = 0
for i in range(q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if t == 1:
        if flag:
            a = (a+n) % (2*n)
            b = (b+n) % (2*n)
        s[a], s[b] = s[b], s[a]
    else:
        flag ^= 1

if flag:
    s = s[n:]+s[:n]

print("".join(s))
