import random
# random.seed(777)

# # 1 <= K <= N <= 5
# N = random.randint(1, 2*10**5)
# print(f"{N}")
# # f = [random.randint(1,N) for _ in range(N)]
# f = [i+1 for i in range(N)]
# print(*f)

N = random.randint(1, 10**5)
M = random.randint(1, 10**9)
print(f"{N} {M}")
A = " ".join(map(str, list(2*random.randint(1, 5*10**8) for _ in range(N))))
print(A)

# # 1 <= K <= N <= 5
# N = random.randint(1, 5)
# K = random.randint(1, N)
# print(f"{N} {K}")

# 開業区切りでの入力の場合
# for _ in range(N):
#     a = random.randint(-10, 10)
#     print(a)

# 配列の場合
# A = " ".join(map(str, list(random.randint(-10, 10) for _ in range(N))))
# print(A)