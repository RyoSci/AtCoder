n = int(input())
s = input()
mod = 10 ** 9 + 7

alphabets = dict()
for i in range(n):
    if s[i] not in alphabets:
        alphabets[s[i]] = 1
    else:
        alphabets[s[i]] += 1

res = 1
for value in alphabets.values():
    res = res * (value + 1) % mod

print((res - 1) % mod)
