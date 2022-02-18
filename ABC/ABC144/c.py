n = int(input())

max_div_num = 1

for i in range(2, int(n**(1/2) + 1)):
    if n % i == 0:
        max_div_num = i

x = max_div_num
y = n // max_div_num

print(x + y - 2)