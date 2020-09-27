s = input() + "+0"
n = len(s)
res = 0
num = int(s[0])
for i in range(n):
    if s[i] == "+":
        if num == 0:
            num = int(s[i + 1])
            pass
        else:
            res += 1
            num = int(s[i + 1])
    elif s[i] == "*":
        # c.py
        num *= int(s[i + 1])
        # c3.py
        num = min(1, num)

        # c1.py
        # if int(s[i + 1]) != 0 and num != 0:
        #     num = 1
        # else:
        #     num = 0

        # # c2.py
        # num = num > 0 and int(s[i + 1]) > 0

print(res)
