n = int(input())
cnt = 0
for i in range(1, 20):
    cnt += 26**i
    if cnt >= n:
        break

digit = i


def binary_search(l, r, x, i):
    tmp = 26**(i-1)
    while l+1 < r:
        m = (l+r)//2
        if m*tmp == x:
            return m
        elif m*tmp < x:
            l = m
        else:
            r = m
    return l


res = ""
for i in range(digit, 0, -1):
    tmp = binary_search(1, 27, n, i)
    if n % 26 == 0 and tmp != 26:
        tmp -= 1
    res += chr(ord("a")+tmp-1)
    n -= (tmp)*26**(i-1)

print(res)
