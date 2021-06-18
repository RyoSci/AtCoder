s = input()
ans = "Yes"

for i in range(len(s)):
    if i % 2 == 0:
        if s[i] in "RUD":
            continue
        else:
            ans = "No"
            break
    else:
        if s[i] in "LUD":
            continue
        else:
            ans = "No"
            break
print(ans)
