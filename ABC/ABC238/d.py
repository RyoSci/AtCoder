from os import sep
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())
pre_process=[2**i for i in range(100)]

q=[]
for i in range(t):
    a,s  = map(int, input().split())
    s-=a*2
    tmp=[0]*60
    for j in range(59,-1,-1):
        if a%2==1:
            tmp[j]=1
        a//=2
    if s<0:
        ans="No"
    else:
        for i in range(59, -1,-1):
            if tmp[59-i]==0 and pre_process[i]<=s:
                s-=pre_process[i]
        if s==0:
            ans="Yes"
        else:
            ans="No"
    q.append(ans)

print(*q,sep="\n")