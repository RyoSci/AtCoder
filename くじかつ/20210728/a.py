n = int(input())
s = input()

for i in range(n):
    if s[i] == "1":
        if i % 2 == 0:
            ans = "Takahashi"
        else:
            ans = "Aoki"
        break

print(ans)
