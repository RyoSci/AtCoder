n, p = map(int, input().split())

ans = 1
if n < 40:
    for i in range(int((p)**(1 / n)) + 1, 1, -1):
        if p % (i ** n) == 0:
            ans = i
            break

print(ans)
