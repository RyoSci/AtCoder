abcd = input()

for i in range(1 << 3):
    res = int(abcd[0])
    op = abcd[0]
    for k in range(3):
        if i >> k & 1:
            res += int(abcd[k + 1])
            op += "+" + abcd[k + 1]
        else:
            res -= int(abcd[k + 1])
            op += "-" + abcd[k + 1]
    if res == 7:
        op += "=7"
        print(op)
        break
