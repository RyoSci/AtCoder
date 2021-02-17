n = int(input())
a = input()
b = input()
c = input()

res = 0
for i in range(n):
    if a[i] == b[i] == c[i]:
        continue
    elif a[i] == b[i] or b[i] == c[i] or c[i] == a[i]:
        res += 1
    else:
        res += 2

print(res)
