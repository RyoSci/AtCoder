# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

q = int(input())

par = dict()
par[-1] = -1

a = dict()
a[-1] = -1

note = dict()

pointer = -1
ans = []
for i in range(q):
    op, *x = list(map(str, input().split()))
    if len(x) > 0:
        x = int(x[0])
    if op == "ADD":
        par[i] = pointer
        pointer = i
        a[pointer] = x
    elif op == "DELETE":
        pointer = par[pointer]
    elif op == "SAVE":
        note[x] = pointer
    else:
        if x not in note:
            pointer = -1
        else:
            pointer = note[x]
    ans.append(a[pointer])

print(*ans)
