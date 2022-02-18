n = int(input())
a = list(map(int, input().split()))
num_map = dict()
for i in range(n):
    if a[i] not in num_map:
        num_map[a[i]] = 1
    else:
        num_map[a[i]] += 1

rest_num_of_over1 = 0
for key, value in num_map.items():
    if value > 1:
        rest_num_of_over1 += 1

tmp_3_list = [a[0]]
for i in range(1, n, 2):
    tmp_3_list += a[i:i + 2]
    tmp_3_list.sort()
    num_map[tmp_3_list[0]] -= 1
    num_map[tmp_3_list[-1]] -= 1
    if num_map[tmp_3_list[0]] == 1:
        rest_num_of_over1 -= 1
    if num_map[tmp_3_list[-1]] == 1:
        rest_num_of_over1 -= 1
    tmp_3_list = [tmp_3_list[1]]
    if rest_num_of_over1 == 0:
        print(n - i - 1)
        break
