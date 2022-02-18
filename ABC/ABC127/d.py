"""
マッピングに配列を使った、配列の大きさが大きすぎて無駄が多い！
テストケースも通らない！
"""
n, m = map(int, input().split())
a = list(map(int, input().split()))

num_map = [0] * (10**5 + 1)
for i in range(n):
    num = a[i]
    num_map[num] += 1

for i in range(m):
    card_num, num = map(int, input().split())
    num_map[num] += card_num

rest_card = n
res_sum = 0
for i in range(10**5, 0, -1):
    tmp = min(num_map[i], rest_card)
    rest_card -= tmp
    res_sum += i * tmp
    if rest_card == 0:
        break

print(res_sum)

