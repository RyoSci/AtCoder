from itertools import combinations
n, m, q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(q)]
# n, m, q = 10, 10, 50
# abcd = [[1, 2, 3, 100] for i in range(q)]

res = 0
# 使う数の種類数を決める
for i in range(1, n+1):
    # 使用上限を超える場合はスキップ
    if m < i:
        continue
    # 使う数の種類を決める
    for j in combinations(range(1, m+1), i):
        # 使う数の境界を決める
        for k in combinations(range(n-1), i-1):
            ki = 0
            a = [0]*n
            # aを作成する
            for l in range(n):
                if ki < i-1 and l <= k[ki]:
                    a[l] = j[ki]
                elif ki == i-1:
                    a[l] = j[ki]
                else:
                    ki += 1
                    a[l] = j[ki]
            # クエリに対して全探索
            tmp = 0
            for qi in range(q):
                ai, bi, ci, di = abcd[qi]
                if a[bi-1]-a[ai-1] == ci:
                    tmp += di
            res = max(res, tmp)

print(res)
