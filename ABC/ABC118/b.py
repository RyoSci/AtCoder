n, m = map(int, input().split())
counter_map = [0] * (m + 1)

for i in range(n):
    k, *a = map(int, input().split())
    for j in a:
        counter_map[j] += 1

res = 0
for i in range(m + 1):
    if counter_map[i] == n:
        res += 1

print(res)