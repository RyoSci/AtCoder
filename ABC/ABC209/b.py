n, x = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if i % 2 == 0:
        cnt += a[i]
    else:
        cnt += a[i]-1

if cnt <= x:
    print("Yes")
else:
    print("No")
