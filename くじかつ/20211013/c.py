import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
s = input().strip()

st = []
for i in range(n):
    if s[i] == "x":
        if len(st) > 0 and st[-1] == "o":
            if len(st) > 1 and st[-2] == "f":
                st.pop()
                st.pop()
                continue
        st.append(s[i])
    else:
        st.append(s[i])

print(len(st))
