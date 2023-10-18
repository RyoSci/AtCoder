# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


# INF = 10**18
INF = (-1, 2**31-1)

"https://tjkendev.github.io/procon-library/python/range_query/ruq_segment_tree.html"


N, M, Q = list(map(int, input().split()))


# N: 処理する区間の長さ

N0 = 2**(N-1).bit_length()
data = [None]*(2*N0)

M0 = 2**(M-1).bit_length()
data1 = [None]*(2*M0)

# 区間[l, r+1)の値をvに書き換える
# vは(t, value)という値にする (新しい値ほどtは大きくなる)


def update(l, r, v):
    L = l + N0
    R = r + N0
    while L < R:
        if R & 1:
            R -= 1
            data[R-1] = v

        if L & 1:
            data[L-1] = v
            L += 1
        L >>= 1
        R >>= 1
# a_iの現在の値を取得


def _query(k):
    k += N0-1
    s = INF
    while k >= 0:
        if data[k]:
            s = max(s, data[k])
        k = (k - 1) // 2
    return s
# これを呼び出す


def update1(l, r, v):
    L = l + M0
    R = r + M0
    while L < R:
        if R & 1:
            R -= 1
            data1[R-1] = v

        if L & 1:
            data1[L-1] = v
            L += 1
        L >>= 1
        R >>= 1
# a_iの現在の値を取得


def _query1(k):
    k += M0-1
    s = INF
    while k >= 0:
        if data1[k]:
            s = max(s, data1[k])
        k = (k - 1) // 2
    return s
# これを呼び出す


def query(k):
    return _query(k)[1]


is_col_last = False
for ii in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        l, r, x = q[1:]
        l -= 1
        r -= 1
        update(l, r+1, x)
    elif q[0] == 2:
        i, x = q[1:]
        i -= 1
        is_col_last = True
        update1(i, i+1, x)
    else:
        i, j = q[1:]
        i -= 1
        j -= 1
        if is_col_last:
