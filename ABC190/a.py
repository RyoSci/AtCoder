a, b, c = map(int, input().split())
if a == b:
    if c == 0:
        win = "Aoki"
    else:
        win = "Takahashi"
elif a > b:
    win = "Takahashi"
else:
    win = "Aoki"

print(win)
