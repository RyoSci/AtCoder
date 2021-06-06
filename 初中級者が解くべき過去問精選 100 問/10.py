n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

all_num = set()
for i in range(1 << n):
    res = 0
    for j in range(n):
        if i >> j & 1:
            res += a[j]
    all_num.add(res)

for i in range(q):
    if m[i] in all_num:
        print("yes")
    else:
        print("no")
