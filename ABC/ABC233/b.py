import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

l, r = map(int, input().split())
s = input().strip()
l -= 1
r -= 1
ans = s[:l]+s[l:r+1][::-1]+s[r+1:]
print(ans)
