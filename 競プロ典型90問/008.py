n = int(input())
s = input()
mod = 10**9+7
atcoder_indexs = [[] for _ in range(len("atcoder"))]
for i in range(n):
    if s[i] in "atcoder":
        i_index = "atcoder".index(s[i])
        atcoder_indexs[i_index].append(i)


def binary_serch(pre_list, serch_i):
    l = 0
    r = len(pre_list)-1
    while l+1 < r:
        m = (l+r)//2
        if pre_list[m] == serch_i:
            return m
        elif pre_list[m] < serch_i:
            l = m
        elif pre_list[m] > serch_i:
            r = m
    else:
        if serch_i <= pre_list[l]:
            return l
        elif pre_list[l] < serch_i <= pre_list[r]:
            return l+1
        elif pre_list[r] < serch_i:
            return r+1


sum_index = [[0] * (len(i) + 1) for i in atcoder_indexs]

for i in range(1, len("atcoder")):
    pre_list = atcoder_indexs[i-1]
    serch_list = atcoder_indexs[i]
    res_index = [0] * (len(serch_list) + 1)
    for ii, serch_i in enumerate(serch_list):
        res_index[ii+1] = binary_serch(pre_list, serch_i)

    for ii in range(len(res_index)):
        if i == 1:
            sum_index[i][ii] = res_index[ii] % mod
            continue

        sum_index[i][ii] = sum_index[i-1][res_index[ii]] % mod

    for ii in range(1, len(sum_index[i])):
        sum_index[i][ii] = (sum_index[i][ii] + sum_index[i][ii-1]) % mod

print(sum_index[-1][-1] % mod)
