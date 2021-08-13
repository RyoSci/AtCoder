n = input()

f = 0
for i in n:
    f += int(i)

if int(n) % f == 0:
    print("Yes")
else:
    print("No")
