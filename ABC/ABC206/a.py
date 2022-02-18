n = int(input())
if int(n*1.08) < 206:
    ans = "Yay!"
elif int(n*1.08) == 206:
    ans = "so-so"
else:
    ans = ":("

print(ans)
