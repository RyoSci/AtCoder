n, k = map(int, input().split())
array = [0]*(10**5+1)

for i in range(n):
    a, b = map(int, input().split())
    array[a] += b

cnt = 0
for i in range(10**5+1):
    cnt += array[i]
    if cnt >= k:
        print(i)
        exit()
