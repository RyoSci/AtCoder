n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = 0
for i in range(1, 1001):
    for j in range(n):
        if a[j] <= i <= b[j]:
            continue
        else:
            break
    else:
        res += 1

print(res)
