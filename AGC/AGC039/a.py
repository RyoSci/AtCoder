s = input()
k = int(input())
n = len(s)

res = 0
tmp = ""
same_num = 1
for i in range(n):
    if tmp == s[i]:
        same_num += 1
    else:
        res += same_num // 2
        tmp = s[i]
        same_num = 1
res += same_num // 2
res *= k

from_first = 0
if s[0] == s[-1]:
    from_first = 0
    for i in range(n):
        if s[i] == s[0]:
            from_first += 1
        else:
            break
    from_end = 0
    for i in range(n - 1, -1, -1):
        if s[-1] == s[i]:
            from_end += 1
        else:
            break
    if from_end % 2 == 1 and from_first % 2 == 1:
        res += k - 1
if n == from_first:
    print(n * k // 2)
else:
    print(res)
