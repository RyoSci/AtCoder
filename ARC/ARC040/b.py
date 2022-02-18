n, r = map(int, input().split())
s = list(input())

res = 0
dis = 0
for i in range(n - 1, -1, -1):
    if s[i] == ".":
        dis = max(dis, i - r + 1)
        res += 1
        for j in range(max(0, i - r + 1), i + 1):
            s[j] = "o"


print(res + dis)
