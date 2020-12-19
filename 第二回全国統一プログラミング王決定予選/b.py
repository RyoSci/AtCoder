n = int(input())
d = list(map(int, input().split()))
# n = 10 ** 5
# d = [0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]
# d = d + [3] * (n-len(d))

mod = 998244353
num_map = [0] * n
for i in range(n):
    num_map[d[i]] += 1


if num_map[0] == 1 and d[0] == 0:
    max_num = max(d)
    ans = 1
    num = 1
    for i in range(n):
        if i > max_num:
            break
        ans = ans * num ** num_map[i] % mod
        num = num_map[i]
else:
    ans = 0

print(ans)
