from copy import deepcopy
from re import L
import sys
import time
import random
from collections import deque
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


def Input():
    """
    入力
    """
    t = []
    n, T = map(int, input().split())
    for i in range(n):
        t.append(list(input()))
    return n, T, t


def count_tiles():
    """
    分布数える
    """
    global tiles
    for i in range(n):
        for j in range(n):
            if t[i][j] == "0":
                si = i
                sj = j
            tiles[int(t[i][j], 16)].append((i, j))
    return si, sj


def check_in_area(i, j, k):
    ni = i+di[k]
    nj = j+dj[k]
    return 0 <= ni < n and 0 <= nj < n


def arange_tiles():
    """
    並び変えて目的の盤面にする
    """
    global t_target
    # 右下は空白にしておく
    t_target[n-1][n-1] = (si, sj)
    tiles[0].pop()
    dq = deque()
    # まずは真ん中に幹を生やして広げて聞く作戦
    for i in range(15, 0, -1):
        if len(tiles[i]) > 0:
            # num, 挿入後のi,j, 元のi,j
            t_target[n//2][n//2] = tiles[i].popleft()
            dq.append((i, n//2, n//2, t_target[n//2][n//2]))
            break

    while len(dq) > 0:
        num, ni, nj, (i, j) = dq.popleft()
        for k in range(4):
            if num >> k & 1 and check_in_area(ni, nj, k):
                for l in range(16):
                    # 自分から下の番号を優先的に採用する
                    nnum = (num-l-1) % 16
                    if len(tiles[nnum]) > 0 and nnum >> dk[k] & 1:
                        nni = ni+di[k]
                        nnj = nj+dj[k]
                        if t_target[nni][nnj] == 0:
                            t_target[nni][nnj] = (i, j)
                            dq.append((nnum, nni, nnj, tiles[nnum].popleft()))
                        break
    # print(*t_target, sep="\n")

    # 余りは詰める
    for i in range(16):
        while len(tiles[i]) > 0:
            dq.append(tiles[i].popleft())

    for i in range(n):
        for j in range(n):
            if t_target[i][j] == 0:
                pi, pj = dq.popleft()
                t_target[i][j] = (pi, pj)
    # print(*t_target, sep="\n")


def check_parity():
    """
    偶奇チェック
    """
    flag = 0
    for i in range(n):
        for j in range(n):
            flag += abs(t_target[i][j][0]-i)
            flag += abs(t_target[i][j][1]-j)
            flag %= 2
    return flag == (n-1-si+n-1-sj) % 2


def chenge_parity():
    global s
    """
    parityが偶になるように入れ替える
    """
    # t_target[0][1], t_target[0][0] = t_target[0][0], t_target[0][1]
    s = s[:-1]


def serch(pi, pj, i, j):
    """
    目的のタイルと同じものを近くから探す
    """
    for ii in range(i, n):
        for jj in range(j, n):
            ni, nj = t_hat[ii][jj]
            if t[ni][nj] == t[pi][pj]:
                return ni, nj


def swap(i, j, k):
    global t_hat, s
    """
    swapする
    """
    s.append(LURD[k])
    ni = i+di[k]
    nj = j+dj[k]
    t_hat[i][j], t_hat[ni][nj] \
        = t_hat[ni][nj], t_hat[i][j]


def left(si, sj, ni, nj, i, j):
    global t_hat, s
    """
    左に目的のタイルを進める
    空白を使ってnjをjにする。
    """
    while nj != j:
        # R
        swap(si, sj, 2)
        sj += 1
        nj -= 1
        if nj == j:
            break
        # 上を通る
        if si == n-1:
            # ULLD
            swap(si, sj, 1)
            si -= 1
            swap(si, sj, 0)
            sj -= 1
            swap(si, sj, 0)
            sj -= 1
            swap(si, sj, 3)
            si += 1
        # 下を通る
        else:
            # DLLU
            swap(si, sj, 3)
            si += 1
            swap(si, sj, 0)
            sj -= 1
            swap(si, sj, 0)
            sj -= 1
            swap(si, sj, 1)
            si -= 1


def right(si, sj, ni, nj, i, j):
    global t_hat, s
    """
    左に目的のタイルを進める
    空白を使ってnjをjにする。
    """
    while nj != j:
        # L
        swap(si, sj, 0)
        sj -= 1
        nj += 1
        if nj == j:
            break
        # 上を通る
        if si == n-1:
            # URRD
            swap(si, sj, 1)
            si -= 1
            swap(si, sj, 2)
            sj += 1
            swap(si, sj, 2)
            sj += 1
            swap(si, sj, 3)
            si += 1
        # 下を通る
        else:
            # DRRU
            swap(si, sj, 3)
            si += 1
            swap(si, sj, 2)
            sj += 1
            swap(si, sj, 2)
            sj += 1
            swap(si, sj, 1)
            si -= 1


def up(si, sj, ni, nj, i, j):
    global t_hat, s
    """
    左に目的のタイルを進める
    空白を使ってnjをjにする。
    """
    while ni != i:
        # D
        swap(si, sj, 3)
        si += 1
        ni -= 1
        if ni == i:
            break
        # 右を通る
        if sj == 0:
            # RUUL
            swap(si, sj, 2)
            sj += 1
            swap(si, sj, 1)
            si -= 1
            swap(si, sj, 1)
            si -= 1
            swap(si, sj, 0)
            sj -= 1


def arange_tate(si, sj):
    """
    """
    # 右端2つは別処理
    swap(si, sj, 1)  # U
    si -= 1
    swap(si, sj, 2)  # R
    sj += 1
    swap(si, sj, 3)  # D
    si += 1
    swap(si, sj, 3)  # D
    si += 1
    swap(si, sj, 0)  # L
    sj -= 1
    swap(si, sj, 1)  # U
    si -= 1
    swap(si, sj, 1)  # U
    si -= 1
    swap(si, sj, 2)  # R
    sj += 1
    swap(si, sj, 3)  # D
    si += 1
    swap(si, sj, 0)  # L
    sj -= 1
    swap(si, sj, 3)  # D
    si += 1
    swap(si, sj, 2)  # R
    sj += 1
    swap(si, sj, 1)  # U
    si -= 1
    swap(si, sj, 1)  # U
    si -= 1
    swap(si, sj, 0)  # L
    sj -= 1
    swap(si, sj, 3)  # D
    si += 1


def match(i, j, pi, pj, t_target):
    """
    """
    # if i > n-2:
    #     pi, pj = t_target[i+1][j]
    # elif j == n-2:
    #     pi, pj = t_target[i][j+1]
    # else:
    #     pi, pj = t_target[i][j]
    # まず同じ列まで寄せる
    ni, nj = serch(pi, pj, i, j)
    # 左に進みたい
    # 左上に空白を置く
    if j < nj:
        # 空白が動かしたいタイルより左にある時
        if sj < nj-1:
            # 隣まで動かす
            while sj < nj-1:
                swap(si, sj, 2)
                sj += 1
        # 空白が動かしたいタイルより右にある時
        else:
            # 同じ行にある時
            if si == ni:
                # 一番下にある時は一つ上を通る
                if ni == n-1:
                    swap(si, sj, 1)
                    si -= 1
                # そうでない時は一つ下を通る
                else:
                    swap(si, sj, 3)
                    si += 1
            # 一つ隣まで動かす
            while sj > nj-1:
                swap(si, sj, 0)
                sj -= 1
        # 真隣に置く
        while si > ni:
            swap(si, sj, 1)
            si -= 1
        while si < ni:
            swap(si, sj, 3)
            si += 1

        left()
        si = i
        sj = j+1

    # 右に進みたい
    # 右上に空白を置く
    if j >= nj:
        # 空白が動かしたいタイルより右にある時
        if nj+1 < sj:
            # 隣まで動かす
            while nj+1 < sj:
                swap(si, sj, 0)
                sj -= 1
        # 空白が動かしたいタイルより左にある時
        else:
            # 同じ行にある時
            if si == ni:
                # 一番下にある時は一つ上を通る
                if ni == n-1:
                    swap(si, sj, 1)
                    si -= 1
                # そうでない時は一つ下を通る
                else:
                    swap(si, sj, 3)
                    si += 1
            # 一つ隣まで動かす
            while sj < nj+1:
                swap(si, sj, 2)
                sj += 1

        right()
        si = i
        sj = j-1

    # 上に進みたい
    # 右上に空白を置く
    if i < ni:
        # 空白が動かしたいタイルより上にある時
        if si < ni-1:
            pass
        # 空白が動かしたいタイルより下にある時
        else:
            # 同じ列にある時
            if si == ni:
                swap(si, sj, 3)
                si += 1
            # 一つ隣まで動かすR
            while sj < nj+1:
                swap(si, sj, 2)
                sj += 1
        # 隣まで動かす
        # D
        while si < ni-1:
            swap(si, si, 3)
            si += 1
        while si > ni-1:
            swap(si, si, 1)
            si -= 1

        # 真上に置く
        while sj > nj:
            swap(si, sj, 0)
            sj -= 1

        up()
        si = i+1
        sj = j


def move():
    global s
    """
    移動関数
    t_hatをt_targetにする
    """
    t_hat = [[(i, j) for j in range(n)] for i in range(n)]
    si, sj = oi, oj
    # targetとするタイルがどこに行ったかをメモ
    tt_taeget = deepcopy(t_target)

    for i in range(n-1):
        for j in range(n-1):
            if i > n-2:
                pi, pj = t_target[i+1][j]
            elif j == n-2:
                pi, pj = t_target[i][j+1]
            else:
                pi, pj = t_target[i][j]
            # # まず同じ列まで寄せる
            # ni, nj = serch(pi, pj, i, j)
            # # 左に進みたい
            # # 左上に空白を置く
            # if j < nj:
            #     # 空白が動かしたいタイルより左にある時
            #     if sj < nj-1:
            #         # 隣まで動かす
            #         while sj < nj-1:
            #             swap(si, sj, 2)
            #             sj += 1
            #     # 空白が動かしたいタイルより右にある時
            #     else:
            #         # 同じ行にある時
            #         if si == ni:
            #             # 一番下にある時は一つ上を通る
            #             if ni == n-1:
            #                 swap(si, sj, 1)
            #                 si -= 1
            #             # そうでない時は一つ下を通る
            #             else:
            #                 swap(si, sj, 3)
            #                 si += 1
            #         # 一つ隣まで動かす
            #         while sj > nj-1:
            #             swap(si, sj, 0)
            #             sj -= 1
            #     # 真隣に置く
            #     while si > ni:
            #         swap(si, sj, 1)
            #         si -= 1
            #     while si < ni:
            #         swap(si, sj, 3)
            #         si += 1

            #     left()
            #     si = i
            #     sj = j+1

            # # 右に進みたい
            # # 右上に空白を置く
            # if j >= nj:
            #     # 空白が動かしたいタイルより右にある時
            #     if nj+1 < sj:
            #         # 隣まで動かす
            #         while nj+1 < sj:
            #             swap(si, sj, 0)
            #             sj -= 1
            #     # 空白が動かしたいタイルより左にある時
            #     else:
            #         # 同じ行にある時
            #         if si == ni:
            #             # 一番下にある時は一つ上を通る
            #             if ni == n-1:
            #                 swap(si, sj, 1)
            #                 si -= 1
            #             # そうでない時は一つ下を通る
            #             else:
            #                 swap(si, sj, 3)
            #                 si += 1
            #         # 一つ隣まで動かす
            #         while sj < nj+1:
            #             swap(si, sj, 2)
            #             sj += 1

            #     right()
            #     si = i
            #     sj = j-1

            # # 上に進みたい
            # # 右上に空白を置く
            # if i < ni:
            #     # 空白が動かしたいタイルより上にある時
            #     if si < ni-1:
            #         pass
            #     # 空白が動かしたいタイルより下にある時
            #     else:
            #         # 同じ列にある時
            #         if si == ni:
            #             swap(si, sj, 3)
            #             si += 1
            #         # 一つ隣まで動かすR
            #         while sj < nj+1:
            #             swap(si, sj, 2)
            #             sj += 1
            #     # 隣まで動かす
            #     # D
            #     while si < ni-1:
            #         swap(si, si, 3)
            #         si += 1
            #     while si > ni-1:
            #         swap(si, si, 1)
            #         si -= 1

            #     # 真上に置く
            #     while sj > nj:
            #         swap(si, sj, 0)
            #         sj -= 1

            #     up()
            #     si = i+1
            #     sj = j
            match(i, j, pi, pj, t_target)
            """"""
            if i == n-2:
                # 下端2つは別処理
                if t_hat[i+1][j] == t_target[i][j]:
                    return False
                else:
                    j += 1
                    pi, pj = t_target[i][j-1]
                    match(i, j, pi, pj, t_target)

                    # arange_yoko(si, sj)
            elif j == n-2:
                # i,j+1->i,jにとi,jをi+1,jに
                if t_hat[i][j+1] == t_target[i][j]:
                    return False
                    # URDDLUURDLDRUULD
                else:
                    i = i+1
                    pi, pj = t_target[i][j]
                    match(i, j, pi, pj, t_target)

                    # arange_tate(si, sj)


def move_random(i, j):
    global s, t_random, si, sj
    """
    ランダム移動関数
    """
    k = random.randint(0, 3)
    if check_in_area(i, j, k):
        s.append(LURD[k])
        ni = i+di[k]
        nj = j+dj[k]
        si, sj = ni, nj
        t_random[ni][nj], t_random[i][j] = t_random[i][j][:], t_random[ni][nj][:]


# 評価関数
def dfs(i, j, pi, pj):
    seen[i][j] = 1
    # ii, jj = t_random[i][j]
    ii, jj = t_target[i][j]
    # 入っている数字を探索
    num = int(t[ii][jj], 16)
    cnt = 1
    for k in range(4):
        if num >> k & 1 and check_in_area(i, j, k):
            ni = i+di[k]
            nj = j+dj[k]
            # nii, njj = t_random[ni][nj]
            nii, njj = t_target[ni][nj]
            # 入っている数字を探索
            nnum = int(t[nii][njj], 16)
            # 逆流禁止
            if ni == pi and nj == pj:
                continue
            # # 既に到達して帰ってきている点ならスキップ
            # if finished[ni][nj] ==1:
            #     continue
            # サイクル検出
            if seen[ni][nj] and not finished[ni][nj]:
                return -1
            if nnum >> dk[k] & 1:
                tmp = dfs(ni, nj, i, j)
                if tmp == -1:
                    return -1
                cnt += tmp
    finished[i][j] = 1

    return cnt


def eval():
    global s_ans, ans, seen, finished
    """
    木の長さを計算してスコアがよければ更新する
    最終盤面に対して操作を行う
    """
    seen = [[0]*n for i in range(n)]
    finished = [[0]*n for i in range(n)]
    res = 0
    for i in range(n):
        for j in range(n):
            """ dfsの確認 """
            if seen[i][j]:
                continue
            size = dfs(i, j, -1, -1)
            # print(size, i, j)
            """"""
            if size == -1:
                continue
            if size > res:
                res = size
                if res == n**2-1:
                    if ans < round(500000*(2-len(s)/T)):
                        ans = round(500000*(2-len(s)/T))
                        s_ans = s[:]
                else:
                    if ans < round(500000*(res*(n**2-1))):
                        ans = round(500000*(res*(n**2-1)))
                        s_ans = s[:]


if __name__ == "__main__":
    # 開始時刻
    tik = time.time()

    s = []
    ans = 0
    s_ans = []

    di = [0, -1, 0, 1]
    dj = [-1, 0, 1, 0]
    LURD = ["L", "U", "R", "D"]
    # 隣が連結になる場合
    dk = [2, 3, 0, 1]
    n, T, t = Input()
    tiles = [deque() for _ in range(16)]
    t_target = [[0]*n for _ in range(n)]
    # t_random = [[(i, j) for j in range(n)] for i in range(n)]
    oi, oj = count_tiles()
    si, sj = oi, oj
    """"""
    # 多段階
    eval()
    for i in range(10**10):

        arange_tiles()
        if check_parity():
            chenge_parity()

        move()
        # move_random(si, sj)
        seen = [[0]*n for i in range(n)]
        finished = [[0]*n for i in range(n)]
        eval()
        if len(s) == T:
            s = []
            si, sj = oi, oj
            # t_random = [[(i, j) for j in range(n)] for i in range(n)]

        tok = time.time()
        if tok - tik > 2.7:
            break
    """"""

    # print(ans)
    # print(tok-tik)
    """"""
    print("".join(s_ans))
