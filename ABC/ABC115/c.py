n, k = map(int, input().split())
h = [0] * n
for i in range(n):
    h[i] = int(input())
h.sort(reverse=True)

l = []
for i in range(n - k + 1):
    l.append(- h[i + k - 1] + h[i])

res = min(l)
print(res)