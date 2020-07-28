s = input()

for i in range(len(s)):
    if (i + 1) % 2 == 1 and s[i] == "L":
        print("No")
        break
    elif (i + 1) % 2 == 0 and s[i] == "R":
        print("No")
        break
else:
    print("Yes")