s = input()

white_num = 0
res = 0
for i in range(len(s) - 1, -1, -1):
    if s[i] == "W":
        white_num += 1
    else:
        res += white_num

print(res)
