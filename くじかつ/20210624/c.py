n = int(input())
h = list(map(int, input().split()))

res = 0
for i in range(1, 101):
    cnt = 0
    flag = False
    for j in range(n):
        if h[j] >= i:
            flag = True
        else:
            if flag:
                cnt += 1
            flag = False
    if flag:
        cnt += 1
    res += cnt

print(res)
