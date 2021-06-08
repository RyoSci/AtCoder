import copy
from itertools import permutations
k = int(input())
queens_ = [["." for _ in range(8)] for i in range(8)]
rows = [i for i in range(8)]
cols = [i for i in range(8)]
for i in range(k):
    r, c = map(lambda x: int(x), input().split())
    queens_[r][c] = "Q"
    rows.remove(r)
    cols.remove(c)


def check_x(r, c):
    for cc in range(8):
        if cc == c:
            continue
        if queens[r][cc] == "Q":
            return False
    else:
        return True


def check_y(r, c):
    for rr in range(8):
        if rr == r:
            continue
        if queens[rr][c] == "Q":
            return False
    else:
        return True


def check_minus1(r, c):
    rr = r-1
    cc = c+1
    while 0 <= rr < 8 and 0 <= cc < 8:
        if queens[rr][cc] == "Q":
            return False
        rr -= 1
        cc += 1
    rr = r+1
    cc = c-1
    while 0 <= rr < 8 and 0 <= cc < 8:
        if queens[rr][cc] == "Q":
            return False
        rr += 1
        cc -= 1
    else:
        return True


def check_plus1(r, c):
    rr = r+1
    cc = c+1
    while 0 <= rr < 8 and 0 <= cc < 8:
        if queens[rr][cc] == "Q":
            return False
        rr += 1
        cc += 1
    rr = r-1
    cc = c-1
    while 0 <= rr < 8 and 0 <= cc < 8:
        if queens[rr][cc] == "Q":
            return False
        rr -= 1
        cc -= 1
    else:
        return True


for i in permutations(rows):
    queens = copy.deepcopy(queens_)
    for ii, jj in zip(i, cols):
        queens[ii][jj] = "Q"
    flag = False
    for r in range(8):
        for c in range(8):
            if queens[r][c] == "Q":
                if check_x(r, c) and check_y(r, c) and check_minus1(r, c) and check_plus1(r, c):
                    continue
                else:
                    flag = True
                    break
        if flag:
            break
    else:
        for i in range(8):
            print("".join(queens[i]))
