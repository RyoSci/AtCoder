n, a, b = map(int, input().split())
s = input()
a_pass = 0
b_pass = 0
for i in range(n):
    res = False
    if s[i] == "a":
        if a_pass + b_pass < a + b:
            res = True
            a_pass += 1

    elif s[i] == "b":
        if a_pass + b_pass < a + b and b_pass + 1 <= b:
            res = True
            b_pass += 1

    if res:
        print("Yes")
    else:
        print("No")
