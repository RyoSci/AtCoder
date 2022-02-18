import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, k = map(int, input().split())
s = input().strip()
INF = -1
dp = [[INF for j in range(26)] for _ in range(n)]

# dp[i][j]<-i番目まで見て、j番目のアルファベットが次に登場するまでの距離
dp[n-1][ord(s[n-1])-ord('a')] = n-1
for i in range(n-2, -1, -1):
    for j in range(26):
        if dp[i+1][j] == INF:
            continue
        dp[i][j] = dp[i+1][j]
    dp[i][ord(s[i])-ord('a')] = i

ans = []
cnt = k
i = 0
while i < n:
    for j in range(26):
        if dp[i][j] == INF:
            continue
        if n-1-dp[i][j] + 1 >= cnt:
            ans.append(chr(ord('a')+j))
            i = dp[i][j]+1
            cnt -= 1
            break
    if cnt == 0:
        break

print(''.join(ans))
