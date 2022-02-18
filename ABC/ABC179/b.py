n = int(input())
counter = 0
for i in range(n):
    d1, d2 = map(int, input().split())
    if d1 == d2:
        counter += 1
    else:
        counter = 0
    if counter == 3:
        print("Yes")
        break
else:
    print("No")
