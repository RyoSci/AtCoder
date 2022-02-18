n = int(input())
a = list(map(int, input().split()))

d = dict()
for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

res = (n*n-n)//2
for key, val in d.items():
    if val >= 2:
        res -= val*(val-1)//2

print(res)
