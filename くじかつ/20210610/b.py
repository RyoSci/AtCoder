s = input()
n = len(s)
for i in range(n):
    if s[i] == "A":
        a = i
        break

for i in range(n-1, -1, -1):
    if s[i] == "Z":
        z = i
        break

print(z-a+1)
