s = input()
n = len(s)
l, r = 0, n - 1
pre_l, pre_r = l, r

x = 0
tmp = ""

while l <= r:
    if s[l] != "x":
        tmp = s[l]
    else:
        l += 1
    if tmp != "":
        if s[r] != "x":
            if tmp == s[r]:
                x += abs(pre_r - r - (l - pre_l))
                pre_l, pre_r = l, r
                l += 1
                r -= 1
                tmp = ""
            else:
                x = -1
                break
        else:
            r -= 1

print(x)
