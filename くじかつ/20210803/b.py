n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

ans = []

for i in range(n):
    ans.append([abs(t-h[i]*0.006-a), i+1])

ans.sort()

print(ans[0][1])
