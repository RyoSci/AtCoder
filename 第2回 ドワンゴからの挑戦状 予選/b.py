n = int(input())
k = list(map(int, input().split()))

l = [0] * n
l[0] = k[0]
for i in range(n - 2):
    l[i + 1] = min(k[i], k[i + 1])

l[-1] = k[-1]

print(*l)
