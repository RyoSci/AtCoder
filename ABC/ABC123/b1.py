import itertools
a_to_e = [int(input()) for i in range(5)]

res = 10 ** 5
for i in itertools.permutations(range(5)):
    sum_min = 0
    for j in range(len(i)):
        if j == 4:
            sum_min += a_to_e[i[j]]
        else:
            sum_min += (a_to_e[i[j]] + 9) // 10 * 10
    res = min(res, sum_min)

print(res)