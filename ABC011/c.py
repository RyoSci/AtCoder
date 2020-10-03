n = int(input())
ng = [int(input()) for i in range(3)]
counter = 0
while n > 0:
    for i in range(3, 0, -1):
        if n in ng or n - i in ng:
            pass
        else:
            n -= i
            counter += 1
            break
    else:
        print("NO")
        break
else:
    if counter <= 100:
        print("YES")
    else:
        print("NO")
