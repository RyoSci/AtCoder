n = input()
mod_map = dict()
mod_map[0] = 0
mod_map[1] = 0
mod_map[2] = 0
total = 0
for i in n:
    tmp = int(i) % 3
    total += tmp
    if tmp not in mod_map:
        mod_map[tmp] = 1
    else:
        mod_map[tmp] += 1

res = -1
if total % 3 == 0:
    res = 0

elif total % 3 == 1:
    if mod_map[1] >= 1:
        res = 1
    elif mod_map[2] >= 2:
        res = 2

elif total % 3 == 2:
    if mod_map[2] >= 1:
        res = 1
    elif mod_map[1] >= 2:
        res = 2

if res == len(n):
    print(-1)
else:
    print(res)
