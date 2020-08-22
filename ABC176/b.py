n = input()
res = 0
for i in range(len(n)):
    res += int(n[i])
if res % 9 == 0:
    print("Yes")
else:
    print("No")
