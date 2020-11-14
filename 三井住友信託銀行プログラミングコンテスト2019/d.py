n = int(input())
s = input()

res = 0
for i in range(0, 1000):
    i = str(i).zfill(3)
    index = 0
    for j in range(n):
        if i[index] == s[j]:
            index += 1
        if index == 3:
            res += 1
            break

print(res)
