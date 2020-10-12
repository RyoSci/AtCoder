s = input()
t = input()
atcoder = "atcoder"
for i in range(len(s)):
    if s[i] == t[i]:
        continue
    elif s[i] == "@" and t[i] in atcoder or t[i] == "@" and s[i] in atcoder:
        continue
    else:
        print("You will lose")
        break
else:
    print("You can win")
