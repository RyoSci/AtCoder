n = int(input())
s = [input() for _ in range(n)]
s = s[::-1]
res = 0

for i in range(n):
    if s[i] == "AND":
        continue
    else:
        res += 2**(n-i)

print(res+1)
