n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))

d_map = dict()
for i in range(n):
    if d[i] not in d_map:
        d_map[d[i]] = 1
    else:
        d_map[d[i]] += 1

ans = "YES"
for i in range(m):
    if t[i] not in d_map or d_map[t[i]] == 0:
        ans = "NO"
        break
    else:
        d_map[t[i]] -= 1

print(ans)
