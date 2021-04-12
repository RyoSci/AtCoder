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

    for i in itertools.permutations(range(10)):
        s_sum = [""] * 3
        for j in range(3):
            for k in s[j]:
                order = alphabets_order[k]
                s_sum[j] += str(i[order])
        s_sum = list(map(int, s_sum))
        if s_sum[0] + s_sum[1] == s_sum[2] and s_sum[0] * s_sum[1] * s_sum[2] != 0:
            for l in range(3):
                if len(str(s_sum[l])) != len(s[l]):
                    break
            else:
                for l in s_sum:
                    print(l)
                exit()
    else:
        print("UNSOLVABLE")
