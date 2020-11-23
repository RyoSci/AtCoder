s = input()
now = 0
res = 0
is_first_down = True

for i in range(len(s)):
    if s[i] == "<":
        now += 1
        res += now
        is_first_down = True
    else:
        if is_first_down:
            is_first_down = False
            before_down_i = i
            befoer_down_n = now

        tmp = i + 1 - before_down_i - 1
        res += tmp
        if tmp >= befoer_down_n:
            res += 1
            befoer_down_n += 1
        now = 0

print(res)
