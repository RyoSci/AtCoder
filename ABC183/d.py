n, w = map(int, input().split())
time_list = [0] * (2 * 10 ** 5 + 1)
for i in range(n):
    s, t, p = map(int, input().split())
    time_list[s] += p
    time_list[t] -= p

ans = "Yes"
for i in range(len(time_list) - 1):
    time_list[i + 1] += time_list[i]
    if time_list[i + 1] > w or time_list[i] > w:
        ans = "No"
        break

print(ans)
