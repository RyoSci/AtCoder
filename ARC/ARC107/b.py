n, k = map(int, input().split())
res = 0
center_num = n
center_index = n + 1

for a_plus_b in range(2, 2 * n + 1):
    c_plus_d = a_plus_b - k
    if 2 <= c_plus_d <= 2 * n:
        res += (center_num - abs(a_plus_b - center_index)) * \
            (center_num - abs(c_plus_d - center_index))

print(res)
