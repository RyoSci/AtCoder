from bisect import bisect_left, bisect_right
n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))

res = 0
for i in range(n):
    res += bisect_left(a, b[i])*(n-bisect_right(c, b[i]))
print(res)
