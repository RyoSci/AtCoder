a, b = map(int, input().split())
l = a+b
r = b

if l >= 15 and r >= 8:
    ans = 1
elif l >= 10 and r >= 3:
    ans = 2
elif l >= 3:
    ans = 3
else:
    ans = 4

print(ans)
