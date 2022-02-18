s = input()

res = 0
previous = s[0]
for i in range(1, len(s)):
    if s[i] == previous:
        res += 1
        previous = str((int(previous) + 1) % 2)
    else:
        previous = s[i]

print(res)