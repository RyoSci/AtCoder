s = input()
n = len(s)
hag = 0
for i in range(n):
    if i >= n - i - 1:
        break
    elif s[i] != s[n - i - 1]:
        hag += 1

print(hag)
