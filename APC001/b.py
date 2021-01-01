n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum_ab = 0
need_time = 0
for i in range(n):
    sum_ab += b[i] - a[i]
    need_time += max(0, (b[i] - a[i] + 1) // 2)

if sum_ab >= need_time:
    print("Yes")
else:
    print("No")
