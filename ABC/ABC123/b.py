dishes = []
n = 5
max_rest = 10
for i in range(n):
    dish = int(input())
    if (dish - 1) % 10 < (max_rest - 1) % 10:
        max_rest = dish
    
    dishes.append((dish + 9) // 10 * 10) 
    
res = sum(dishes) - (max_rest + 9) // 10 * 10 + max_rest
print(res)
# print(dishes)

