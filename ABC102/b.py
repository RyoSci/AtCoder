n = int(input())
a = list(map(int, input().split()))
a.sort()
res = a[-1] - a[0]
print(res)
