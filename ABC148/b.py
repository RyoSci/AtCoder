n = int(input())
s, t = input().split()
res_str = ""
for i in range(n):
    res_str += s[i]
    res_str += t[i]

print(res_str)