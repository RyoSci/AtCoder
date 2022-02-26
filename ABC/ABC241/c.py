import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
s = []
for i in range(n):
    si = input().strip()
    # tmp = []
    # for j in si:
    #     if j == "#":
    #         tmp.append(1)
    #     else:
    #         tmp.append(0)
    # s.append(tmp)
    # s.append(list(si))
    s.append(si)


def tate(i, j):
    res = False
    for dl, dr in [(1, 1), (2, 0), (0, 2)]:
        l = i
        r = i
        cnt = 1
        # lについて
        while 1:
            if l == 0:
                break
            l -= 1
            if s[l][j] == "#":
                # if s[l][j] == 1:
                cnt += 1
            elif dl > 0:
                dl -= 1
                cnt += 1
            else:
                break
        # rについて
        while 1:
            if r == n-1:
                break
            r += 1
            if s[r][j] == "#":
                # if s[r][j] == 1:
                cnt += 1
            elif dr > 0:
                dr -= 1
                cnt += 1
            else:
                break
        if cnt >= 6:
            res = True
            break
    return res


def yoko(i, j):
    res = False
    for dl, dr in [(1, 1), (2, 0), (0, 2)]:
        l = j
        r = j
        cnt = 1
        # lについて
        while 1:
            if l == 0:
                break
            l -= 1
            if s[i][l] == "#":
                # if s[i][l] == 1:
                cnt += 1
            elif dl > 0:
                dl -= 1
                cnt += 1
            else:
                break
        # rについて
        while 1:
            if r == n-1:
                break
            r += 1
            if s[i][r] == "#":
                # if s[i][r] == 1:
                cnt += 1
            elif dr > 0:
                dr -= 1
                cnt += 1
            else:
                break
        if cnt >= 6:
            res = True
            break
    return res


def naname0(i, j):
    res = False
    for dl, dr in [(1, 1), (2, 0), (0, 2)]:
        x = i
        y = j
        cnt = 1
        # lについて
        while 1:
            if x == n-1 or y == 0:
                break
            x += 1
            y -= 1
            if s[x][y] == "#":
                # if s[x][y] == 1:
                cnt += 1
            elif dl > 0:
                dl -= 1
                cnt += 1
            else:
                break
        x = i
        y = j
        # rについて
        while 1:
            if x == 0 or y == n-1:
                break
            x -= 1
            y += 1
            if s[x][y] == "#":
                # if s[x][y] == 1:
                cnt += 1
            elif dr > 0:
                dr -= 1
                cnt += 1
            else:
                break
        if cnt >= 6:
            res = True
            break
    return res


def naname1(i, j):
    res = False
    for dl, dr in [(1, 1), (2, 0), (0, 2)]:
        x = i
        y = j
        cnt = 1
        # lについて
        while 1:
            if x == 0 or y == 0:
                break
            x -= 1
            y -= 1
            if s[x][y] == "#":
                # if s[x][y] == 1:
                cnt += 1
            elif dl > 0:
                dl -= 1
                cnt += 1
            else:
                break
        x = i
        y = j
        # rについて
        while 1:
            if x == n-1 or y == n-1:
                break
            x += 1
            y += 1
            if s[x][y] == "#":
                # if s[x][y] == 1:
                cnt += 1
            elif dr > 0:
                dr -= 1
                cnt += 1
            else:
                break
        if cnt >= 6:
            res = True
            break
    return res


ans = "No"
for i in range(n):
    for j in range(n):
        if s[i][j] == ".":
            # if s[i][j] == 0:
            continue
        if tate(i, j) or yoko(i, j) or naname0(i, j) or naname1(i, j):
            ans = "Yes"
            print(ans)
            exit()

print(ans)
