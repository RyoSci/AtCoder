n = int(input())
ba = []

for i in range(n):
    a, b = map(int, input().split())
    ba.append([b, a])

ba.sort()

now = 0
ans = "Yes"
for i in range(n):
    if now + ba[i][1] <= ba[i][0]:
        now += ba[i][1]
    else:
        ans = "No"
        break

print(ans)
