n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))


def binary_search(a, bi):
    l = 0
    r = n - 1
    while l + 1 < r:
        m = (l + r) // 2
        if a[m] >= bi:
            r = m
        else:
            l = m
    if bi <= a[l]:
        return l
    elif a[l] < bi <= a[r]:
        return l + 1
    elif a[r] < bi:
        return r + 1


res = 0
ab = [0] * (n + 1)
for i in range(n):
    ab[i + 1] = binary_search(a, b[i]) + ab[i]

for i in range(n):
    res += ab[binary_search(b, c[i])]
print(res)
