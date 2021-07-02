n = int(input())
s = list(input())
t = list(input())

res = 0
j = 0
for i in range(n):
    if s[i] != t[i]:
        while j < n:
            if s[j] == "1" and j > i:
                s[i] = t[i]
                s[j] = "0"
                res += j-i
                break
            j += 1

if s == t:
    print(res)
else:
    print(-1)
