import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))

st = dict()
for i in d:
    if i not in st:
        st[i] = 0
    st[i] += 1


ans = "YES"
for i in t:
    if i not in st or st[i] == 0:
        ans = "NO"
        break
    else:
        st[i] -= 1

print(ans)
