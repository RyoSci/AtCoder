n = int(input())
a = list(map(int, input().split())) + [0]
success = 1
success_map = dict()
for i in range(n):
    if a[i + 1] > a[i]:
        success += 1
    else:
        if success not in success_map:
            success_map[success] = 1
        else:
            success_map[success] += 1
        success = 1

res = 0
for key, value in success_map.items():
    res += key * (key + 1) // 2 * value

print(res)
