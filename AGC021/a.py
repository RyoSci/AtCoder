n = input()
for i in range(len(n) - 1, 0, -1):
    if n[i] != "9":
        res = 9 * (len(n) - 1) + int(n[0]) - 1
        break
else:
    res = 0
    for i in n:
        res += int(i)

print(res)
