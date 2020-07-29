s = input()

counter_map = dict()
for i in range(4):
    if s[i] not in counter_map:
        counter_map[s[i]] = 1
    else:
        counter_map[s[i]] += 1

for i in counter_map.values():
    if i == 2:
        pass
    else:
        print("No")
        break
else:
    print("Yes")