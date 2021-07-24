n = int(input())
b = list(map(int, input().split()))
a = [b[0]]+[0]*(n-2)+[b[-1]]

for i in range(1, n-1):
    a[i] = min(b[i-1], b[i])

print(sum(a))
