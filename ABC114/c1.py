import itertools

n = int(input())
list_3_5_7 = ["3", "5", "7"]

res = 0
for i in range(3, 10):
    tmp_product_list = list(itertools.product(list_3_5_7, repeat = i))
    for tmp_list in tmp_product_list:
        tmp_str = "".join(tmp_list)
        if len(set(tmp_str)) == 3 and int(tmp_str) <= n:
            res += 1

print(res)