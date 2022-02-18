n = int(input())
p = list(map(int, input().split()))

wrong = 0
for i in range(1, n + 1):
    if i == p[i - 1]:
        pass
    else:
        wrong += 1

if wrong <= 2:
    print("YES")
else:
    print("NO")
