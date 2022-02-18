import itertools
n = int(input())
a = [0, 3, 5, 7]
ans = []
res = 0
for i in itertools.product(a, repeat = 9):
    val = 0
    for j in range(len(i)):
        val += 10 ** j * i[j]
    # print(val)
    tmp = str(val)
    if val <= n and len(set(tmp)) == 3 and "0" not in tmp:
        res += 1
        ans.append(val)

ans.sort()
print(res)
# print(ans)