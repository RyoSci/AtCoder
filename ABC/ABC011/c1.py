n = int(input())
ng = [int(input()) for i in range(3)]
counter = 0
ans = True
while n > 0:
    for i in range(3, 0, -1):
        if n in ng or n - i in ng:
            pass
        else:
            n -= i
            counter += 1
            break
    else:
        ans = False
        break
else:
    if counter > 100:
        ans = False

if ans:
    print("YES")
else:
    print("NO")
