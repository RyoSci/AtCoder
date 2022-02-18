n = int(input())
res = 10 ** 5
sum_num = 0
for nine in range(6, -1, -1):
    for a in range(8, -1, -1):
        if sum_num + 9 ** nine * a <= n:
            sum_num += 9 ** nine * a

        for six in range(7, -1, -1):
            for b in range(5, -1, -1):
                if sum_num + 6 ** six * b <= n:
                    sum_num += 6 ** six * b

        tmp = n - 9 ** nine - 6 ** six + 2
        print(tmp)
        if tmp > 0:
            res = min(res, tmp)

print(res)
