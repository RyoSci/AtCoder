n = int(input())
s = [input() for _ in range(n)]
t = input()

l = 1
r = n+1

for i in range(n):
    if s[i] == t:
        continue
    if "?" in s[i]:
        si = s[i].replace("?", "z")
        sj = s[i].replace("?", "a")
    else:
        si = s[i]
        sj = s[i]
    tmp = sorted([si, t])
    for i in range(2):
        if tmp[i] == t:
            l += i
            break
    tmp = sorted([sj, t])
    for i in range(2):
        if tmp[-i-1] == t:
            r -= i
            break

# print(l, r)
print(*range(l, r+1))
