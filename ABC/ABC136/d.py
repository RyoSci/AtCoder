s = input()
n = len(s)

dis = [0] * n
rs = []

for i in range(n):
    if s[i] == "R":
        rs.append(i)
    else:
        for j in rs:
            dis[j] = i - j
        rs = []

ls = []
for i in range(n - 1, -1, -1):
    if s[i] == "L":
        ls.append(i)
    else:
        for j in ls:
            dis[j] = j - i
        ls = []

max_dis = max(dis)
ans = [0] * n
for i in range(n):
    if s[i] == "R":
        ans[i + dis[i] - (max_dis - dis[i] + max_dis % 2) % 2] += 1
    else:
        ans[i - dis[i] + (max_dis - dis[i] + max_dis % 2) % 2] += 1

print(*ans)
