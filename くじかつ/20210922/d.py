import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

if n > 1:
    ans = []
    cnt = 0
    for i in range(1, n):
        cnt += i
        ans.append(i)
        if cnt + i+1 > n:
            break

    for i in range(n-cnt):
        ans[-i-1] += 1

    print(*ans, sep="\n")
else:
    print(1)
