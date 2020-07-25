n = int(input())
a = list(map(int, input().split()))

money = 1000

for i in range(1, n):
    if a[i] > a[i - 1]:
        money = (money // a[i-1]) * a[i] + money % a[i-1]
    else:
        pass

print(money)