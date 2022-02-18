n ,l = map(int, input().split())
apple = []
for i in range(n):
    apple.append(l + i)

min_num = 10 ** 5
sum_num = sum(apple)
for i in range(n):
    tmp = abs(sum_num - (sum_num - apple[i]))
    if tmp < min_num:
        min_num = min(tmp, min_num)
        flag = apple[i]

if flag >= 0:
    print(sum(apple) - min_num)
else:
    print(sum(apple) + min_num)