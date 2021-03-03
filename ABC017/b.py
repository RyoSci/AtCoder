x = input()

ans = "YES"
while len(x) > 0:
    if x[0] == "o" or x[0] == "k" or x[0] == "u":
        x = x[1:]
        continue
    elif len(x) >= 2 and x[0:2] == "ch":
        x = x[2:]
        continue
    else:
        ans = "NO"
        break

print(ans)
