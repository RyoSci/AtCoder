n, k = map(int, input().split())
res = [0]*n
for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for ai in a:
        res[ai-1] += 1

ans = 0
for i in range(n):
    if res[i] == 0:
        ans += 1

print(ans)
