n = int(input())
name_num = dict()
for i in range(n):
    s = input()
    if s not in name_num:
        name_num[s] = 1
    else:
        name_num[s] += 1

max_value = 0
name = ""
for key, value in name_num.items():
    if value > max_value:
        name = key
        max_value = value

print(name)
