n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))

d.sort()
t.sort()

j = 0
ans = "YES"
for i in range(m):
    while j < n:
        if t[i] == d[j]:
            j += 1
            break
        else:
            j += 1
    else:
        ans = "NO"

print(ans)
