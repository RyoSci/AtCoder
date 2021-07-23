n = int(input())
a = [0]+list(map(int, input().split()))

memo = [0]*(n+1)

for i in range(n, 0, -1):
    j = 2
    tmp = 0
    while i*j <= n:
        tmp += memo[i*j]
        j += 1
    if tmp % 2 != a[i]:
        memo[i] = 1

ans = []
for i in range(1, n+1):
    if memo[i] == 1:
        ans.append(i)

print(len(ans))
if len(ans) != 0:
    print(*ans)
