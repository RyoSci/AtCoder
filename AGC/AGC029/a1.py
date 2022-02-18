s = input()
b_pos_sum = 0
b_num = 0

for i in range(len(s)):
    if s[i] == "B":
        b_pos_sum += i
        b_num += 1

res = (len(s) - b_num + len(s) - 1) * b_num // 2 - b_pos_sum
print(res)
