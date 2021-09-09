import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

s = input().strip()

st = []

for i in s:
    if i == "B":
        if len(st) > 0:
            st.pop()
    else:
        st.append(i)

print(*st, sep="")
