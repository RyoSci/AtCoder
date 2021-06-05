import bisect
n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))

res = 0
for i in range(n):
    res += bisect.bisect_left(a, b[i]) * (n-bisect.bisect_right(c, b[i]))

print(res)
