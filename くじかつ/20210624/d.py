from bisect import bisect_left
n = int(input())
a = sorted(list(map(int, input().split())))
p = a.pop()
p_harf = p/2

r = bisect_left(a, p_harf)
r = min(r, n-2)
l = max(0, r-1)

if abs(p-2*a[l]) < abs(p-2*a[r]):
    print(p, a[l])
else:
    print(p, a[r])
