import sys
from types import CodeType
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def main():
    # h, w = map(int, input().split())
    # s = [list(input().strip()) for _ in range(h)]
    h = 2000
    w = 2000
    s = [list("."*w) for _ in range(h)]
    grid = [[0]*w for _ in range(h)]

    def procced(x, y, dx, dy, candidate):
        nx = x+dx
        ny = y+dy
        if not(0 <= nx < h and 0 <= ny < w):
            return candidate
        if s[nx][ny] == "#":
            return candidate
        candidate.append([nx, ny])
        return procced(nx, ny, dx, dy, candidate)

    # def procced(x, y, dx, dy, candidate):
    #     nx = x+dx
    #     ny = y+dy
    #     while 0 <= nx < h and 0 <= ny < w:
    #         if s[nx][ny] == "#":
    #             return candidate
    #         candidate.append([nx, ny])
    #         nx = nx+dx
    #         ny = ny+dy
    #     return candidate

    bools = [[0]*w for _ in range(h)]
    total = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                continue
            total += 1
            # for dx, dy in [[0, 1], [0, -1]]:
            if bools[i][j] == 1:
                continue
            candidate = [i, j]
            candidate = procced(i, j, 0, 1, [candidate])
            for ci, cj in candidate:
                if bools[ci][cj] == 1:
                    break
                grid[ci][cj] += len(candidate)
                bools[ci][cj] = 1

    bools = [[0]*w for _ in range(h)]
    for j in range(w):
        for i in range(h):
            if s[i][j] == "#":
                continue
            # for dx, dy in [[1, 0], [-1, 0]]:
            if bools[i][j] == 1:
                continue
            candidate = [i, j]
            candidate = procced(i, j, 1, 0, [candidate])
            for ci, cj in candidate:
                if bools[ci][cj] == 1:
                    break
                grid[ci][cj] += len(candidate)-1
                bools[ci][cj] = 1

    res = 0
    mod = 10**9+7
    for i in range(h):
        for j in range(w):
            if grid[i][j] > 0:
                res += (pow(2, grid[i][j], mod)-1) * \
                    pow(2, total-grid[i][j], mod)
                # res += (2**(grid[i][j])-1)*2**(total-grid[i][j])
                res %= mod

    print(res)


if __name__ == "__main__":
    main()
