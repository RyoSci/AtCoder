n = int(input())
a = []

for i in range(n):
    syougen_num = int(input())
    ai = []
    for j in range(syougen_num):
        xi_yi = list(map(int, input().split()))
        ai.append(xi_yi)
    a.append(ai)

res = 0
for i_bin in range(1 << n):
    syougen_list = [[0, 0] for i in range(n)]
    one_counter = 0
    for keta in range(n):
        # 1を正直者にした
        if i_bin >> keta & 1 == 1:
            one_counter += 1
            for i_syougen in a[keta]:
                #yi :0は不親切 :1は正直者 
                xi, yi = i_syougen
                syougen_list[xi - 1][yi] += 1
    for i_syougen in range(n):
        if syougen_list[i_syougen][0] >= 1 and syougen_list[i_syougen][1] >= 1:
            break
        elif syougen_list[i_syougen][0] >= 1 and i_bin >> i_syougen & 1 == 1:
            break
        elif syougen_list[i_syougen][1] >= 1 and i_bin >> i_syougen & 1 == 0:
            break
    else:
        res = max(res, one_counter)
        flag = i_bin
    # print(syougen_list, i_bin, one_counter, flag)
print(res)



