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

if max_sum_num == m:
    print(count_max_card)
else:
    print(0)

"""
imos方を使わずに書いた場合
"""
n, m = map(int, input().split())
cardid_2_num_map = [0] * (10**5 + 2)

for i in range(m):
    l, r = map(int, input().split())
    for j in range(l, r + 1):
        cardid_2_num_map[j] += 1

max_sum_num = max(cardid_2_num_map)
count_max_card = cardid_2_num_map.count(max_sum_num)

if max_sum_num == m:
    print(count_max_card)
else:
    print(0)