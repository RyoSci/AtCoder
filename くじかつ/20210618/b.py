n, a, b = map(int, input().split())
s = input()

total = 0
inter = 0
for i in range(n):
    if s[i] == "a":
        if total < a+b:
            print("Yes")
            total += 1
        else:
            print("No")
    elif s[i] == "b":
        if total < a+b and inter < b:
            print("Yes")
            total += 1
            inter += 1
        else:
            print("No")
    else:
        print("No")
