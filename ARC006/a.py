e = input().split()
b = input()
l = input().split()
res = 0
bonus = 0
for i in range(6):
    if l[i] in e:
        res += 1
    elif l[i] == b:
        bonus = 1

ans = 0
if res == 6:
    ans = 1
elif res == 5 and bonus:
    ans = 2
elif res == 5:
    ans = 3
elif res == 4:
    ans = 4
elif res == 3:
    ans = 5

print(ans)
