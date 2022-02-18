n = int(input())
s = [int(input()) for i in range(n)]
sum_list = [0]

for i in range(n):
    for j in range(len(sum_list)):
        sum_list.append(sum_list[j] + s[i])

sum_list.sort(reverse=True)
for i in sum_list:
    if i % 10 != 0:
        print(i)
        break
    else:
        pass
else:
    print(0)
