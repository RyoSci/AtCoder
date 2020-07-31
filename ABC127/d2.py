"""
マッピングに配列を使った場合、配列の大きさが大きすぎて無駄が多かったから
配列サイズの無駄を減らした。m回の操作の際に入力をそのまま受け取る。
"""
n, m = map(int, input().split())
a = list(map(int, input().split()))

num_map = []
for i in range(n):
    num = a[i]
    num_map.append([num, 1])


for i in range(m):
    card_num, num = map(int, input().split())
    num_map.append([num, card_num])

num_map.sort(reverse=True)

rest_card = n
res_sum = 0
for i in range(len(num_map)):
    num, card_num = num_map[i]
    can_use = min(card_num, rest_card)
    rest_card -= can_use
    res_sum += num * can_use

    if rest_card == 0:
        break

print(res_sum)