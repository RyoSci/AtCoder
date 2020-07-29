n = int(input())
res = 0
for i in range(6):
    if n // (10 ** i) >= 10 and (i + 1) % 2 == 1:
        res += 9 * (10 ** i)
    elif 1 <= n // (10 ** i) < 10 and (i + 1) % 2 == 1:
        res += ((n // (10 ** i)) - 1) * (10 ** i)
        res += (n % (10 ** i)) + 1 # i になってなかった
print(res)

# res_2 = 0
# for i in range(1, n + 1):
#     if len(str(i)) % 2 == 1:
#         res_2 += 1

# print(res_2)
