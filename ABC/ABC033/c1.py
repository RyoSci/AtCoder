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
        # num *= int(s[i + 1])
        if int(s[i + 1]) != 0 and num != 0:
            num = 1
        else:
            num = 0

print(res)
