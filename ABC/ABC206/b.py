n = int(input())

cnt = 0
for i in range(1, 10**6):
    cnt += i
    if cnt >= n:
        break

print(i)
