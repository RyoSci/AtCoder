# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
def input(): return sys.stdin.readline().rstrip()


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    a = list(map(int, input().split()))

    pos_cnt = []
    cnt = 1
    pos = 0
    cat = s[0]
    for i in range(n-1):
        if s[i] == s[i+1]:
            cnt += 1
        else:
            pos_cnt.append([cat, pos, cnt])
            cat = s[i+1]
            cnt = 1
            pos = i+1

    pos_cnt.append([cat, pos, cnt])

    # print(pos_cnt)
    ans = 0
    for cat, pos, cnt in pos_cnt:
        if cat == "0":
            continue
        tmp = a[max(0, pos-1):pos+cnt]
        tmp.sort(reverse=True)
        ans += sum(tmp[:cnt])
    print(ans)
