n = int(input())
s = input()
num_map = dict()
for i in range(10):
    num_map[str(i)] = 0

for i in range(n):
    num_map[str(s[i])] += 1

res = 0
for i in range(0, 1000):
    i = str(i).zfill(3)
    tmp_map = dict()
    flag = False
    for index in range(3):
        if i[index] not in tmp_map:
            tmp_map[str(i[index])] = 1
        else:
            tmp_map[str(i[index])] += 1
    for num in tmp_map.keys():
        if tmp_map[num] > num_map[num]:
            flag = True
            break
    if flag:
        continue
    index = 0
    for j in range(n):
        if i[index] == s[j]:
            index += 1
        if index == 3:
            res += 1
            break

print(res)
