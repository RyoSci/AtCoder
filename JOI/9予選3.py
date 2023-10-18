# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

# どこで変えるかを全探索
# 色の変え方は２通り
# 変えるまでは積んでいく
# 連鎖が終わったタイミングで、直前の連鎖が4以上なら消す
# 消した場合直前と連鎖できるか確認する


n = int(input())
s = [int(input()) for _ in range(n)]


def check(sj):
    if st[-1][-1] >= 4:
        st.pop()
        if len(st) > 0 and st[-1][0] == sj:
            st[-1][-1] += 1
        else:
            st.append([sj, 1])
    else:
        st.append([sj, 1])


def pile(sj):
    if len(st) == 0:
        st.append([sj, 1])
    elif st[-1][0] != sj:
        check(sj)
    else:
        st[-1][-1] += 1


ans = INF
for c in range(1, 3):
    for i in range(n):

        st = []
        # 変えるまで
        for j in range(i):
            pile(s[j])

        # 変える
        si = (s[i] - 1 + c) % 3 + 1
        pile(si)

        # 変えた後
        for j in range(i+1, n):
            pile(s[j])

        # 最後が連続の場合
        if len(st) > 0 and st[-1][-1] >= 4:
            st.pop()

        # 数える
        cnt = 0
        while len(st):
            _, num = st.pop()
            cnt += num
        ans = min(ans, cnt)

print(ans)
