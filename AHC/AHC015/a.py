# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

# a = list(map(int, input().split()))
# cnt = [0]*3

# for i in range(100):
#     cnt[a[i]-1] += 1

# tmp = []
# for i in range(3):
#     tmp.append((cnt[i], i))

# tmp.sort()
# most = tmp[-1][-1]

# for i in range(100):
#     if a[i] == most:
#         print("B", flush=True)
#     else:
#         print("L", flush=True)

#     t = int(input())
n = 10
board = [[-1]*n for _ in range(n)]


def move(x):
    if x == "L":
        for i in range(n):
            k = 0
            for j in range(n):
                if board[i][j] != -1:
                    board[i][k] = board[i][j]
                    if k != j:
                        board[i][j] = -1
                    k += 1

    elif x == "R":
        for i in range(n):
            k = n-1
            for j in range(n-1, -1, -1):
                if board[i][j] != -1:
                    board[i][k] = board[i][j]
                    if k != j:
                        board[i][j] = -1
                    k -= 1
    if x == "F":
        for j in range(n):
            k = 0
            for i in range(n):
                if board[i][j] != -1:
                    board[k][j] = board[i][j]
                    if k != i:
                        board[i][j] = -1
                    k += 1
    if x == "B":
        for j in range(n):
            k = n-1
            for i in range(n-1, -1, -1):
                if board[i][j] != -1:
                    board[k][j] = board[i][j]
                    if k != i:
                        board[i][j] = -1
                    k -= 1


board[0][0] = 1
board[1][1] = 2
print(*board, sep="\n")
move("F")

print(*board, sep="\n")
