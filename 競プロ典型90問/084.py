n = int(input())
s = input()

res = 0
j = 1
for i in range(n):
    while j < n:
        if s[i] != s[j]:
            res += n-j
            break
        j += 1

print(res)
