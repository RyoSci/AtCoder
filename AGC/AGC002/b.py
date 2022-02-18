n, m = map(int, input().split())
red_possible = [1] + [0] * (n - 1)
card_nums = [1] * n

for i in range(m):
    x, y = map(lambda x: int(x) - 1, input().split())
    if red_possible[x] == 1:
        if card_nums[x] == 1:
            red_possible[x] = 0
        red_possible[y] = 1
    card_nums[x] -= 1
    card_nums[y] += 1

print(sum(red_possible))
