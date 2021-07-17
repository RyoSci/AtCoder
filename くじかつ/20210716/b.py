n = int(input())
p = list(map(int, input().split()))

d = [0]*(2*10**5+10)

index = 0

for i in range(n):
    d[p[i]] = 1
    while 1:
        if d[index] == 0:
            break
        else:
            index += 1
    print(index)
