n = int(input())
a = list(map(int, input().split()))

memo = [0]*n

for i in range(n-1, -1, -1):
    if memo[i] == a[i]:
        memo[i] = 0
        continue
    for j in range(1, int((i+1)**0.5)+1):
        if (i+1) % j == 0:
            memo[j-1] += 1
            memo[j-1] %= 2
            if (i+1)//j != j:
                memo[(i+1)//j-1] += 1
                memo[(i+1)//j-1] %= 2
    memo[i] = 1

m = 0
ans = []
for i in range(n):
    if memo[i] == 1:
        m += 1
        ans.append(i+1)

print(m)
if len(ans) != 0:
    print(*ans)
