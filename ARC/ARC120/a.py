n = int(input())
a = list(map(int, input().split()))

max_a = [0]*(n+1)
tmp = 0
for i in range(n):
    tmp = max(tmp, a[i])
    max_a[i+1] = tmp

last = 0
res = 0

for i in range(n):
    dis = max_a[i+1]-max_a[i]
    last = last+dis+a[i]
    res = res+dis*(i) + last
    print(res)
