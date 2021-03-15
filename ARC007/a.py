x = input()
s = input()
ans = ""
for i in s:
    if i == x:
        continue
    ans += i
print(ans)
