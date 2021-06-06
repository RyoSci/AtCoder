n, k = map(int, input().split())
a = list(map(int, input().split()))
# a = [10**9 for i in range(n)]


money = 10**11
for i in range(1 << (n-1)):
    cnt = 1
    highest = a[0]
    tmp = 0
    for j in range(n-1):
        if i >> j & 1:
            cnt += 1
            tmp += max(0, highest-a[j+1]+1)
            highest = max(highest+1, a[j+1])
        else:
            if a[j+1] > highest:
                cnt += 1
                highest = a[j+1]
    if cnt >= k:
        money = min(money, tmp)

print(money)
