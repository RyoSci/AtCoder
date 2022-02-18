s = input()
alphabet_dict = dict()
for i in "ABCDEF":
    alphabet_dict[i] = 0

for i in s:
    alphabet_dict[i] += 1

res = []
for i in "ABCDEF":
    res.append(alphabet_dict[i])

print(*res)
