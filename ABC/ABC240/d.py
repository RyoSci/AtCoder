import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

from collections import deque

st = deque()

n = int(input())
a = list(map(int, input().split()))

ans=[]
now=0
for i in range(n):
    if len(st) >0 and st[-1][0]==a[i]:
        st[-1][1]+=1
        now+=1
    else:
        st.append([a[i], 1])
        now+=1

    if st[-1][0]==st[-1][1]:
        now-=st[-1][1]
        st.pop()
    ans.append(now)

print(*ans)