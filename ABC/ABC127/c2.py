
n, m = map(int, input().split())
cardid_2_num_map = [0] * (10**5 + 2)

for i in range(m):
    l, r = map(int, input().split())
    cardid_2_num_map[l] += 1
    cardid_2_num_map[r + 1] -= 1

for i in range(1, n + 1):
    cardid_2_num_map[i] += cardid_2_num_map[i - 1]

max_sum_num = max(cardid_2_num_map)

count_max_card = cardid_2_num_map.count(max_sum_num)
in_a_low_value = 0
"""
連続した部分を数えて検証する方式だと重なっていない部分を落としきれない！！！
重なっていなくても最大値が1つ存在しているときに、１を出力して誤答している。
"""
flag = False
for i in range(n + 2):
    if cardid_2_num_map[i] == max_sum_num:
        in_a_low_value += 1
        flag = True
    elif flag:
        break

if in_a_low_value == count_max_card:
    print(in_a_low_value)
else:
    print(0)



    