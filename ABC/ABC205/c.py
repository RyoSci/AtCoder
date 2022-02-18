a, b, c = map(int, input().split())

if a == b or (abs(a) == abs(b) and c % 2 == 0):
    ans = "="
elif a >= 0 and b >= 0:
    if a > b:
        ans = ">"
    else:
        ans = "<"
elif a >= 0 and b < 0:
    if c % 2 == 1:
        ans = ">"
    else:
        if abs(a) > abs(b):
            ans = ">"
        else:
            ans = "<"
elif a < 0 and b >= 0:
    if c % 2 == 1:
        ans = "<"
    else:
        if abs(a) > abs(b):
            ans = ">"
        else:
            ans = "<"
else:
    if c % 2 == 1:
        if a > b:
            ans = ">"
        else:
            ans = "<"
    else:
        if a > b:
            ans = "<"
        else:
            ans = ">"

print(ans)
