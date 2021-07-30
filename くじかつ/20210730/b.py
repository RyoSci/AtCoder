n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))

res = 0
j = 0
k = 0
for i in range(n):
    while j < n:
        if a[i] < b[j]:
            while k < n:
                if a[i] < b[j] < c[k]:
                    res += 1
                    k += 1
                    break
                else:
                    k += 1
            j += 1
            break
        else:
            j += 1

print(res)
