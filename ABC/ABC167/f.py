# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = []
t = []
for i in range(n):
    si = input()
    st = []
    for sij in si:
        if len(st) > 0 and sij == ")" and st[-1] == "(":
            st.pop()
        else:
            st.append(sij)
    l = 0
    r = 0
    for sij in st:
        if sij == "(":
            l += 1
        else:
            r += 1
    s.append("".join(st))
    if r == 0:
        t.append((-INF, -l, i))
    elif l == 0:
        t.append((INF, -l, i))
    else:
        t.append((r, -l, i))

# s.sort()
t.sort()
ss = ""
for _, _, i in t:
    ss += s[i]

# print(ss)
st = []
for si in ss:
    if len(st) > 0 and si == ")" and st[-1] == "(":
        st.pop()
    else:
        st.append(si)

if len(st) == 0:
    print("Yes")
else:
    print("No")
