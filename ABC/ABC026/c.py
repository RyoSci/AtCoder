n = int(input())
super_to_sub = dict()
super_to_sub[1] = []
for i in range(n - 1):
    b = int(input())
    super_to_sub[b].append(i + 2)
    super_to_sub[i + 2] = []

keys = sorted(list(super_to_sub.keys()), reverse=True)
salaly_map = [0] * n
for key in keys:
    if super_to_sub[key] == []:
        salaly_map[key - 1] = 1
    else:
        max_sub = 0
        min_sub = 10 ** 7
        for i in super_to_sub[key]:
            max_sub = max(max_sub, salaly_map[i - 1])
            min_sub = min(min_sub, salaly_map[i - 1])
        salaly_map[key - 1] = max_sub + min_sub + 1
print(salaly_map[0])
