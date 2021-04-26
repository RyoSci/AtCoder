n = int(input())
a = sorted(list(map(int, input().split())))


def binary_search(x):
    l = 0
    r = len(a) - 1
    m = (l + r) // 2
    if len(a) == 1:
        return abs(a[l] - x)
    while l + 1 != r:
        if a[m] == x:
            return 0
        elif a[m] < x:
            l = m
            m = (l + r) // 2
        else:
            r = m
            m = (l + r) // 2

    return min(abs(a[l] - x), abs(a[r] - x))


q = int(input())
for i in range(q):
    b = int(input())
    print(binary_search(b))
