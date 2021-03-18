n, m = map(int, input().split())
name = input()
kit = input()

name_dict = dict()
kit_dict = dict()

for i in name:
    if i not in name_dict:
        name_dict[i] = 1
    else:
        name_dict[i] += 1

for i in kit:
    if i not in kit_dict:
        kit_dict[i] = 1
    else:
        kit_dict[i] += 1

ans = -1
for key, val in name_dict.items():
    if not key in kit_dict:
        ans = -1
        break
    ans = max(ans, (val + kit_dict[key] - 1) // kit_dict[key])

print(ans)
