import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

l = 0
r = 2*10**9


def cal(line):
    res = 0
    for i in range(n):
        res += max(0, a[i]-line+1)
    return res


def binary_search(l, r):
    while l+1 < r:
        m = (l+r)//2
        num = cal(m)
        if num == k:
            return m
        elif num < k:
            r = m
        else:
            l = m
    return r


line = binary_search(l, r)
res = 0
for i in range(n):
    if a[i] >= line:
        res += (a[i]+line)*(a[i]-line+1)//2

res += (line-1)*(k-cal(line))
print(res)
