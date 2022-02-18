n = int(input())
a = list(map(int, input().split()))
if sum(a) % n != 0:
    print(-1)
else:
    ave = sum(a) // n
    for i in range(n):
        a[i] -= ave

    bridges = [0] * (n - 1)
    for i in range(n):
        if a[i] != 0:
            a[i + 1] += a[i]
            bridges[i] = 1

    print(sum(bridges))
