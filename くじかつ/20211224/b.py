import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

ans=[]
for i in range(t):
    n = int(input())
    if n%4==0:
        ans.append("Even")
    elif n%2==0:
        ans.append("Same")
    else:
        ans.append("Odd")

print(*ans,sep="\n")