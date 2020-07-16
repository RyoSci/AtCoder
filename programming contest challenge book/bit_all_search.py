n = 4
a = (1, 2, 4, 7)
k = 13

# n = int(input())
# a = [int(i) for i in input().split()]
# k = int(input())

for i in range(2 ** n):
    tmp_sum = 0
    tmp_num_list = []
    for j in range(n):
        if bin(i >> j)[-1] == "1":
            tmp_sum += a[j]
            tmp_num_list.append(a[j])
    if tmp_sum == k:
        print("Yes", tmp_num_list)
        break
else:
    print("No")
