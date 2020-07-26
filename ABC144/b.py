n = int(input())
is_yes = False
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == n:
            is_yes = True

if is_yes:
    print("Yes")
else:
    print("No")