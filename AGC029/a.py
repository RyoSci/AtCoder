s = input()

black_num = 0
res = 0
for i in range(len(s)):
    if s[i] == "B":
        res += len(s) - 1 - black_num - i
        black_num += 1

print(res)
