# n , k = map(int, input().split())
# h = list(map(int, input().split()))
# h.sort(reverse = True)

# l = 0
# r = n - 1
# res_index = 0
# while l + 1 != r:
#     middle = (r + l) // 2
#     if h[middle] <= k:
#         l = middle
#         res_index = middle 
#     else:
#         r = middle
#         res_index = middle 
#     print(l, middle, r, res_index)
# print(res_index)
