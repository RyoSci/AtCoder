# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
def input(): return sys.stdin.readline().rstrip()


t = int(input())
for _ in range(t):
    s = input()
    indexes = []
    for i, j in enumerate(s):
        indexes.append([ord(j)-ord("a")+1, i])

    st = indexes[0][0]
    ed = indexes[-1][0]

    if st > ed:
        indexes.sort(reverse=True)
    else:
        indexes.sort()

    for i, (j, k) in enumerate(indexes):
        if j == st:
            st_id = i
            break
    indexes = indexes[::-1]
    for i, (j, k) in enumerate(indexes):
        if j == ed:
            ed_id = len(s)-1-i
            break
    print(abs(st-ed), ed_id-st_id+1)
    ans = [1]
    indexes = indexes[::-1]
    # print(st, ed)
    # print(st_id, ed_id)
    # print(indexes)
    for i in range(st_id, ed_id+1):
        tmp = indexes[i][1]+1
        if tmp in {1, len(s)}:
            continue
        ans.append(indexes[i][1]+1)
    ans.append(len(s))
    print(*ans)
