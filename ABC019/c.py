n = int(input())
a = list(map(int, input().split()))
box = set()
for i in range(n):
    tmp = a[i]
    while tmp % 2 == 0:
        tmp //= 2
    box.add(tmp)

print(len(box))
