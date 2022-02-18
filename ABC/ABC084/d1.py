like_2017 = [0] * (10 ** 5 + 1)
for i in range(3, 10 ** 5 + 1, 2):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        for j in range(2, int(((i + 1) // 2) ** 0.5) + 1):
            if (i + 1) // 2 % j == 0:
                break
        else:
            like_2017[i] = 1

sum_like_2017 = [0] * (10 ** 5 + 1)
for i in range(1, 10 ** 5):
    sum_like_2017[i] = sum_like_2017[i - 1] + like_2017[i]

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(sum_like_2017[r] - sum_like_2017[l - 1])
