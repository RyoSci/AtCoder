t = int(input())

ans = []
for i in range(t):
    n = int(input())
    if n % 6 == 0:
        ans.append("Yes")
    else:
        ans.append("No")

for i in range(t):
    print(ans[i])
