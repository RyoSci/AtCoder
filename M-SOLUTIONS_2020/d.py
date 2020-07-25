n = int(input())
a = list(map(int, input().split()))
money  = 1000
stock = 0
min_price = a[0]
max_price = a[0]
is_first_time_of_drop = False
for i in range(1, n):
    if a[i] > max_price:
        max_price = a[i]
        is_first_time_of_drop = True
        if i == n - 1:
            money = (money // min_price) * max_price + money % min_price
    elif a[i] == max_price:
        if i == n - 1:
            money = (money // min_price) * max_price + money % min_price
        continue
    else:
        if is_first_time_of_drop:
            money = (money // min_price) * max_price + money % min_price
            min_price = a[i]
            max_price = a[i]
            is_first_time_of_drop = False
        else:
            if a[i] < min_price:
                min_price = a[i]
                max_price = a[i]
            elif a[i] == min_price:
                continue
            else:
                is_first_time_of_drop = True
print(money)



# for i in range(n):
#     if a[i] <= min_price:
#         min_price = a[i]
#     else:
#         max_price = a[i]
#         if a[i] >= max_price:
#             max_price = a[i]
#             if i == n - 1:
#                 money = (money // min_price) * max_price + money % min_price
#         else:
#             money = (money // min_price) * max_price + money % min_price
#             min_price = a[i]
#             max_price = a[i]
# print(money)
