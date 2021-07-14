n = int(input())
a = list(map(int, input().split()))
total = 0
for i in range(n):
    total ^= a[i]

ans = [0]*n
for i in range(n):
    ans[i] = total ^ a[i]

print(*ans)
