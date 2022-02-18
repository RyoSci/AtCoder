n = int(input())
a = list(map(int, input().split()))
ans = []
for i in range(n):
    ans.append([a[i], i])

ans.sort()

print(ans[-2][1]+1)
