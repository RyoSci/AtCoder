n = int(input())
res = ""
while n > 0:
    res += chr(ord("a")+(n-1) % 26)
    n = (n-1) // 26

print(res[::-1])
