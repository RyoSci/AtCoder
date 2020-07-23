import math
n = int(input())
ten_counter = 0
exp_index = math.log(10 ** 18, 5)
if n % 2 == 0:
    n //= 2
    # rangeの範囲をlogとったら if: break 不要
    for i in range(1, int(exp_index) + 1):
        if n // (5 ** i) == 0:
            break
        else:
            ten_counter += n // (5 ** i)
    # else:
    #     print("finish")
else:
    pass

print(ten_counter)