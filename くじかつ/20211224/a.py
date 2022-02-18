import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

s = input().strip()
ans=700+100*s.count('o')
print(ans)