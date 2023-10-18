INF = 10**18

n = int(input())
c = []
a = []
for i in range(n):
    ci = int(input())
    c.append(ci)
    ai = set(map(int, input().split()))
    a.append(ai)

x = int(input())

now = INF
for i in range(n):
    if x in a[i]:
        now = min(now, c[i])

ans = []
for i in range(n):
    if now == c[i] and x in a[i]:
        ans.append(i+1)

print(len(ans))
print(*ans)
