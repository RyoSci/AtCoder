n, w = map(int, input().split())
s = []
t = []
for i in range(n):
    si, ti, pi = map(int, input().split())
    s.append([si, pi])
    t.append([ti, pi])

s.sort()
t.sort()
s_index = 0
t_index = 0
time = 0
water = 0
ans = "Yes"
while s_index < n:
    if t[t_index][0] == time:
        water -= t[t_index][1]
        t_index += 1
    else:
        if s[s_index][0] == time:
            water += s[s_index][1]
            s_index += 1
        else:
            time += 1
    if water > w:
        ans = "No"
        break
print(ans)
