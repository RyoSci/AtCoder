n , k =map(int, input().split())
a = list(map(int, input().split()))

for i in range(k, n):
    if a[i - k] < a[i]:
        print("Yes")
    else:
        print("No")

# n , k =map(int, input().split())
# a = list(map(int, input().split()))
# a_mul = [0] * n
# mul = 1
# for i in range(n):
#     if i < k:
#         mul *= a[i]
#     else:
#         mul = mul * a[i] // a[i - k]
#     a_mul[i] = mul

# for i in range(n - k):
#     if a_mul[k + i - 1] < a_mul[k + i]:
#         print("Yes")
#     else:
#         print("No") 