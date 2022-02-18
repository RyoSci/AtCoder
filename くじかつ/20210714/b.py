s = input()

t = set()
ans = "yes"
for i in s:
    if i not in t:
        t.add(i)
    else:
        ans = "no"
        break

print(ans)
