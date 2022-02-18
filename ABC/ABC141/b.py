s = input()

for i in range(1, len(s) + 1):
    if i % 2 == 1:
        if s[i - 1] == "R" or s[i - 1] == "U" or s[i - 1] == "D":
            continue
        else:
            print("No")
            break
    else:
        if s[i - 1] == "L" or s[i - 1] == "U" or s[i - 1] == "D":
            continue
        else:
            print("No")
            break
else:
    print("Yes")