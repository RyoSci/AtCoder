import itertools

s = [input() for _ in range(3)]
alphabets = {}
for si in s:
    for i in si:
        if i not in alphabets:
            alphabets[i] = 1

if len(alphabets) >= 11:
    print("UNSOLVABLE")
else:
    alphabets_order = {}
    for i, key in enumerate(sorted(list(alphabets.keys()))):
        alphabets_order[key] = i
    for i in "123456789": 
        for ii in itertools.permutations("0123456789", 9):
            i = i + str(ii)
            print(i)
        # for i in itertools.permutations(range(10)):
            for j in range(3):
                order = alphabets_order[s[j][0]]
                if i[order] == 0:
                    break
            else:

                # s_sum = s[::]
                s_sum = [""] * 3
                for j in range(3):
                    # for key, val in alphabets_order.items():
                    #     s_sum[j] = s_sum[j].replace(key, str(i[val]))
                    for k in s[j]:
                        order = alphabets_order[k]
                        s_sum[j] += i[order]
                if int(s_sum[0]) + int(s_sum[1]) == int(s_sum[2]) and int(s_sum[0]) * int(s_sum[1]) * int(s_sum[2]) != 0:
                    # for l in range(3):
                    #     if len(s_sum[l]) != len(s[l]):
                    #         break
                    # else:
                        for l in s_sum:
                            print(l)
                        exit()
        else:
            print("UNSOLVABLE")

