n = int(input())
ans = []
for x in range(n - 162, n - 1 + 1):
    if x > 0:
        fx = 0
        for i in str(x):
            fx += int(i)
        if x + fx == n:
            ans.append(x)

print(len(ans))
for x in ans:
    print(x)
