"""
マッピングに配列を使った場合、配列の大きさが大きすぎて無駄が多かったから
辞書型に変更。
"""
n, m = map(int, input().split())
a = list(map(int, input().split()))

num_map = dict()
for i in range(n):
    num = a[i]
    if num not in num_map:
        num_map[num] = 1
    else:
        num_map[num] += 1

for i in range(m):
    card_num, num = map(int, input().split())
    if num not in num_map:
        num_map[num] = card_num
    else:
        num_map[num] += card_num

num_map_list = list(num_map.keys())
num_map_list.sort(reverse=True)

rest_card = n
res_sum = 0
for i in range(len(num_map_list)):
    num = num_map_list[i]
    some_num = num_map[num]
    can_use = min(some_num, rest_card)
    rest_card -= can_use
    res_sum += num * can_use

    if rest_card == 0:
        break

print(res_sum)

