n = int(input())
l = list(map(int, input().split()))
num_map = dict()

for i in range(n):
    if l[i] not in num_map:
        num_map[l[i]] = 1
    else:
        num_map[l[i]] += 1

num_list = sorted(list(num_map.keys()))
m = len(num_list)
res = 0
for i in range(m - 2):
    for j in range(i + 1, m - 1):
        for k in range(j + 1, m):
            if num_list[i] + num_list[j] > num_list[k]:
                res += num_map[num_list[i]] * num_map[num_list[j]] * num_map[num_list[k]]
print(res)