n, m = sorted(list(map(int, input().split())))

if n == 2 or m == 2:
    ans = 0
elif n == 1 and m == 1:
    ans = 1
elif n == 1:
    ans = m-2
else:
    ans = (n-2)*(m-2)

print(ans)
