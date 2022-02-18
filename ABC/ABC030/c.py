n, m = map(int, input().split())
x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i = 0
j = 0
cnt = 0
now = 0
while i < n:
    if now <= a[i]:
        now = a[i] + x
        while j < m:
            if now <= b[j]:
                now = b[j] + y
                cnt += 1
                break
            j += 1
    i += 1
print(cnt)
