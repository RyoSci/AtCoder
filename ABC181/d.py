s = input()
s_map = dict()

for i in s:
    if i not in s_map:
        s_map[i] = 1
    else:
        s_map[i] += 1
s_map["0"] = 0

flag = False
if int(s) < 100:
    for i in range(8, 100, 8):
        i = sorted(list(str(i)))
        s = sorted(list(s))
        if i == s:
            flag = True
            break
else:
    for i in range(104, 1000, 8):
        i = str(i)
        i_map = dict()
        for j in i:
            if j not in i_map:
                i_map[j] = 1
            else:
                i_map[j] += 1
        for key in i_map.keys():
            if key in s_map:
                if s_map[key] < i_map[key]:
                    break
            else:
                break
        else:
            flag = True
            break

if flag:
    print("Yes")
else:
    print("No")
