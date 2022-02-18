import copy
h, w, k =map(int,input().split())
masu = []

for i in range(h):
    line = list(input())
    masu.append(line)

masu_tmp = copy.deepcopy(masu)
res=0
for i in range(2 ** h):
    masu_tmp = copy.deepcopy(masu)
    binary_i = format(i, 'b')
    i_len=len(binary_i)
    binary_i = "0"*(h-i_len)+binary_i
    for ii in range(len(binary_i)):
        if binary_i[ii] == "1":
            masu_tmp[ii]=list("-"*w)
    masu_tmp_2 = copy.deepcopy(masu_tmp)
    for j in range(2 ** w):
        masu_tmp_2 = copy.deepcopy(masu_tmp)
        counter = 0
        binary_j = format(j, 'b')
        i_len=len(binary_j)
        binary_j = "0"*(w-i_len)+binary_j
        # print(binary_j)
        for l in range(len(binary_j)):
            if binary_j[l] == "1":
                for m in range(h):
                    masu_tmp_2[m][l]="-"
                # print(m,l)
        for n in range(h):
            for o in range(w):
                if masu_tmp_2[n][o] == "#":
                    counter +=1
                # print(n,o)
        if counter == k:
            res += 1
        # print(masu_tmp_2)
print(res)
# print(masu_tmp)
