n = int(input())
a = sorted(list(map(int, input().split())))
cnt = 0
total = sum(a)
res = 10**15
for i, x in enumerate(a):
    cnt += x
    tmp = n*(x/2)+total-(x)*(n-i-1)-cnt
    res = min(res, tmp)

print(res/n)
