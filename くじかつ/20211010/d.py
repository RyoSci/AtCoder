import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

s = input().strip()
abc = [0]*3

for i in s:
    if i == "a":
        abc[0] += 1
    elif i == "b":
        abc[1] += 1
    else:
        abc[2] += 1

abc.sort()
m_abc = max(abc)
if m_abc-1 <= abc[0] <= m_abc and m_abc-1 <= abc[1] <= m_abc:
    print("YES")
else:
    print("NO")
