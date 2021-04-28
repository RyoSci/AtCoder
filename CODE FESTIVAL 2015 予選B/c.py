n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

ans = "YES"
j = 0
for i in range(m):
    while j < n:
        if b[i] <= a[j]:
            j += 1
            ans = "YES"
            break
        else:
            j += 1
            ans = "NO"
    else:
        ans = "NO"

print(ans)
