n = int(input())
s = input()
r = 0
for i in range(n):
    if s[i] == "R":
        r += 1
if r > n - r:
    print("Yes")
else:
    print("No")
