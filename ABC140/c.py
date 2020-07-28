n = int(input())
b = list(map(int, input().split()))
a = [0] * n
a[0] = b[0]
for i in range(n - 1):
    if a[i] <= b[i]:
        pass
    else:
        a[i] = b[i]
    a[i + 1] = b[i]

print(sum(a)) 