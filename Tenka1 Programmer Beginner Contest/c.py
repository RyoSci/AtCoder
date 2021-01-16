from collections import deque
n = int(input())
a = sorted([int(input()) for _ in range(n)])

d = deque()
l = 1
r = n - 2
d.append(a[-1])
d.append(a[0])


def put(lr):
    if abs(d[0] - a[lr]) >= abs(d[-1] - a[lr]):
        d.appendleft(a[lr])
    else:
        d.append(a[lr])


while l <= r:
    if l == r:
        put(r)
    else:
        if l % 2 == 0:
            d.append(a[l])
        else:
            d.appendleft(a[l])
        if r % 2 == n % 2:
            d.append(a[r])
        else:
            d.appendleft(a[r])
    l += 1
    r -= 1

ans = 0
# print(d)
for i in range(n - 1):
    ans += abs(d[i + 1] - d[i])
print(ans)
