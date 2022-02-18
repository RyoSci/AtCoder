n = int(input())
s1 = input()
s2 = input()
mod = 10 ** 9 + 7
s1 += "1"
state = 0
res = 1
i = 0
while i < n:
    if s1[i] == s1[i + 1]:
        if state == 0:
            res = res * 6 % mod
        elif state == 1:
            res = res * 2 % mod
        else:
            res = res * 3 % mod
        state = 2
        i += 2
    else:
        if state == 0:
            res = res * 3 % mod
        elif state == 1:
            res = res * 2 % mod
        else:
            res = res * 1 % mod
        state = 1
        i += 1

print(res % mod)
