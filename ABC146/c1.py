a, b, x = map(int,input().split())
res = 0
for i in range(1, 19 , 1):
    tmp = (x - b * i) // a
    if tmp * a + len(str(tmp)) * b <= x:
        res = max(res, tmp)
        # break
    # print(res)
res = max(0, res)
print(min(10 ** 9, res))
print(len("-1"))

#1つのケースがどうしても通らない
# a, b, x = map(int,input().split())
# res = 0
# for i in range(1, 19 , 1):
#     tmp = (x - b * i) // a
#     if len(str(tmp)) == i and tmp * a + len(str(tmp)) * b <= x:
#         res = max(res, tmp)
#         # break
#     # print(res)
# res = max(0, res)
# print(min(10 ** 9, res))
