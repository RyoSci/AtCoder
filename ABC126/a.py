n, k = map(int, input().split())
s = input()

res = ""
for i in range(n):
    if i + 1 == k:
        res += s[i].lower() 
    else:
        res += s[i]

print(res)