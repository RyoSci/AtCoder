from queue import Queue
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)

q = [[0] for _ in range(31)]
index = 29
two = 2 ** 29
for i in range(n):
    while index >= 0:
        if two <= a[i]:
            q[index + 1].append(a[i])
            break
        else:
            index -= 1
            two //= 2

index = 29
j = 0
q[index + 1].sort(reverse=True)
for i in range(m):
    while index >= 0:
        if q[index + 1][j] != 0:
            a = q[index + 1][j]
            q[index].append(a // 2)
            q[index + 1][j] = 0
            j += 1
            break
        else:
            index -= 1
            q[index + 1].sort(reverse=True)
            j = 0

ans = 0
for i in range(1, 31):
    ans += sum(q[i])

print(ans)
