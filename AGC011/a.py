n, c, k = map(int, input().split())
t = sorted([int(input()) for i in range(n)])

buses = 0
earliest = t[0]
now_person = 1
for i in range(1, n):
    if t[i] <= earliest + k:
        if now_person + 1 <= c:
            now_person += 1
        else:
            buses += 1
            earliest = t[i]
            now_person = 1
    else:
        buses += 1
        earliest = t[i]
        now_person = 1

print(buses + 1)
