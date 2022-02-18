# def make_divisors(n):
#     lower_divisors , upper_divisors = [], []
#     i = 1
#     while i*i <= n:
#         if n % i == 0:
#             lower_divisors.append(i)
#             if i != n // i:
#                 upper_divisors.append(n//i)
#         i += 1
#     return lower_divisors + upper_divisors[::-1]
# make_divisors(10**7)
# # print(make_divisors(10**7))
# n=int(input())
# res=0
# for i in range(1,n+1):
#     res+=i*len(make_divisors(i))

# print(res)

#AC
n = int(input())
res = 0
for i in range(1, n+1):
    res += (int(n / i) * (i + int(n / i) * i)) // 2
print(res)

#別解思考
n = int(input())
res = 0
for i in range(1, n // 2 +1):
    res += (int(n / i) * (i + int(n / i) * i)) // 2
res += (n + n // 2 +1) * (n - n // 2 ) //2
print(res)