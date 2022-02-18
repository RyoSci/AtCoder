a, b, k = map(int,input().split())
# for i in range(k):
#     if a >= 1:
#         a -= 1
#     elif b >= 1:
#         b -= 1
#     else:
#         continue

tmp = min(k, a)
a -= tmp
k -= tmp
b = max(0, b - k)

print(a, b)