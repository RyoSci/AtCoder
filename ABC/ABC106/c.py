s = input()
k = int(input())

one_counter = 0
for i in range(len(s)):
    if s[i] != "1":
        break
    else:
        one_counter += 1

if s[0] == "1":
    if k <= one_counter:
        res = s[0]
    else:
        res = s[one_counter]
else:
    res = s[0]

print(res)