from bisect import bisect_left
n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

res = 10**18
for i in range(n):
    index = bisect_left(b, a[i])
    if index == m:
        index -= 1
    res = min(res, abs(a[i]-b[index-1]), abs(a[i]-b[index]))

print(res)
