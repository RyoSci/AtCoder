import sys
s0 = sys.argv[1]
s1 = sys.argv[2]
s2 = sys.argv[3]
# a = [input()[::-1] for _ in range(3)]
a = [i[::-1] for i in [s0, s1, s2]]

c = set("".join(a))
if len(c) > 10:
    print('UNSOLVABLE')
    exit(0)
if len(a[2]) < max(len(a[0]), len(a[1])):
    print('UNSOLVABLE')
    exit(0)


def print_solution(a, d):
    for num in a:
        s = "".join([str(d[c]) for c in reversed(num)])
        print(s)
    exit(0)


taken = [0] * 10 + [1] * 10


def dfs(a, d, i, j, summ, taken):
    if i == len(a[-1]):
        if (summ == 0):
            for z in range(len(a)):
                if d[a[z][-1]] == 0:
                    return
            print_solution(a, d)
            exit(0)

        return
    if j == 2:
        if a[j][i] in d:
            if d[a[j][i]] == summ % 10:
                dfs(a, d, i+1, 0, summ // 10, taken)
        else:
            if taken[summ % 10]:
                return
            taken[summ % 10] = 1
            d[a[j][i]] = summ % 10
            dfs(a, d, i+1, 0, summ // 10, taken)
            del d[a[j][i]]
            taken[summ % 10] = 0
        return

    if i >= len(a[j]):
        dfs(a, d, i, j+1, summ, taken)
        return
    if a[j][i] in d:
        dfs(a, d, i, j+1, summ + d[a[j][i]], taken)
        return
    for cand in range(10):
        if taken[cand]:
            continue
        taken[cand] = 1
        d[a[j][i]] = cand
        dfs(a, d, i, j + 1, summ + cand, taken)
        del d[a[j][i]]
        taken[cand] = 0
    return


dfs(a, dict(), 0, 0, 0, taken)

print('UNSOLVABLE')
