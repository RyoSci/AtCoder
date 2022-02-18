n = int(input())
l = list(map(int, input().split()))
l.sort()


def binary_search(c: int, l: list):
    left = 0
    right = n - 1
    while left + 1 != right:
        mid = (left + right) // 2
        if l[mid] < c:
            left = mid
        else:
            right = mid
    if l[right] < c:
        return right
    else:
        return left


res = 0
for a in range(n - 2):
    for b in range(a + 1, n - 1):
        c = l[a] + l[b]
        res += binary_search(c, l) - b

print(res)
