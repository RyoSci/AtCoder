n = int(input())
a = sorted(list(map(int, input().split())) + [0, 10**9+1])
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())) + [0, 10**9+1])


def binary_search_left(x, i):
    l = 0
    r = len(x)-1
    m = (r+l)//2
    while l+1 < r:
        if x[m] < i:
            l = m
        else:
            r = m
        m = (r+l)//2
    return m


def binary_search_right(x, i):
    l = 0
    r = len(x)-1
    m = (r+l)//2
    while l+1 < r:
        if x[m] <= i:
            l = m
        else:
            r = m
        m = (r+l)//2
    return m


res = 0
for i in range(n):
    res += binary_search_left(a, b[i])*(n-binary_search_right(c, b[i]))
print(res)
