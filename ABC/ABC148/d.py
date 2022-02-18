n = int(input())
a = list(map(int,input().split()))
order_counter = 1
is_not_minus = False
for i in range(n):
    if a[i] == order_counter:
        order_counter += 1
        is_not_minus = True

if is_not_minus:
    print(n - order_counter + 1)
else:
    print(-1)