n = int(input())
a = list(map(int, input().split()))
a.sort()
sum_a = sum(a)
res = 10**15
tmp = 0
for i, x in enumerate(a):
    tmp += x
    x /= 2
    res = min(res, n*x+sum_a-tmp-2*x*(n-i-1))

print(res/n)
