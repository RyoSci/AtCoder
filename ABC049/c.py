s = input()
s = s[::-1]
t = ["dream", "dreamer", "erase", "eraser"]

i = 0
while i < len(s) - 7 + 1:
    for j in t:
        if s[i:i + len(j)] == j[::-1]:
            i += len(j)
            break
    else:
        print("NO")
        break
else:
    for j in t:
        if s[i:] == j[::-1] or s[i:] == "":
            print("YES")
            break
    else:
        print("NO")
