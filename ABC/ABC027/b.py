n = int(input())
a = list(map(int, input().split()))
if sum(a) % n != 0:
    print(-1)
else:
    ave = sum(a) // n
    for i in range(n):
        a[i] -= ave

    bridges = [0] * (n - 1)
    i = 0
    while i < n - 1:
        if a[i] > 0:
            tmp = a[i]
            for j in range(i + 1, n):
                tmp += a[j]
                if tmp <= 0:
                    for k in range(i, j):
                        bridges[k] = 1
                    a[j] = tmp
                    i = j - 1
                    break
        elif a[i] == 0:
            pass
        else:
            tmp = a[i]
            for j in range(i + 1, n):
                tmp += a[j]
                if tmp >= 0:
                    for k in range(i, j):
                        bridges[k] = 1
                    a[j] = tmp
                    i = j - 1
                    break
        i += 1
    print(sum(bridges))
