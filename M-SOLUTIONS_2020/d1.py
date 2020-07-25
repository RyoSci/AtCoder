n = int(input())
a = list(map(int, input().split()))

state_of_up_or_down = False
money = 1000
min_price = a[0]
max_price = a[0]
for i in range(1, n):
    if a[i] > a[i - 1]:
        max_price = a[i]
        state_of_up_or_down = True
        if i == n - 1:
            money = (money // min_price) * max_price + money % min_price
    elif a[i] == a[i - 1]:
        if i == n - 1:
            money = (money // min_price) * max_price + money % min_price        
        pass
    else:
        if state_of_up_or_down:
            money = (money // min_price) * max_price + money % min_price
            state_of_up_or_down = False
        min_price = a[i]
    # print(money, min_price, state_of_up_or_down)
print(money)