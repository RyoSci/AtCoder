# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

table = dict()
for i in range(n):
    if a[i] not in table:
        table[a[i]] = 0
    table[a[i]] += 1


for i in range(m):
    b, c = map(int, input().split())
    if c not in table:
        table[c] = 0
    table[c] += b

table_keys = list(table.keys())
table_keys.sort(reverse=True)

ans = []
for i in table_keys:
    for j in range(table[i]):
        ans.append(i)
        if len(ans) >= n:
            print(sum(ans[:n]))
            exit()
