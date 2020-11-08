n = int(input())
s = input()
l = 0
l_tmp = 0
lf = 0
flag = True
for i in range(n):
    if s[i] == ".":
        l_tmp += 1
        if flag:
            lf += 1
    else:
        l = max(l, l_tmp)
        l_tmp = 0
        flag = False

print(lf, l_tmp + max(0, l - lf - l_tmp))
