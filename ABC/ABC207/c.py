n = int(input())

tlr = [list(map(int, input().split())) for _ in range(n)]
tlr.sort()

res = 0
for i in range(n-1):
    ti, li, ri = tlr[i]
    for j in range(i+1, n):
        tj, lj, rj = tlr[j]
        if ti == 1:
            if tj == 1:
                if not (rj < li or ri < lj):
                    res += 1
            if tj == 2:
                if not (rj <= li or ri < lj):
                    res += 1
            if tj == 3:
                if not (rj < li or ri <= lj):
                    res += 1
            if tj == 4:
                if not (rj <= li or ri <= lj):
                    res += 1
        if ti == 2:
            if tj == 2:
                if not (rj <= li or ri <= lj):
                    res += 1
            if tj == 3:
                if not (rj < li or ri <= lj):
                    res += 1
            if tj == 4:
                if not (rj <= li or ri <= lj):
                    res += 1
        if ti == 3:
            if tj == 3:
                if not (rj <= li or ri <= lj):
                    res += 1
            if tj == 4:
                if not (rj <= li or ri <= lj):
                    res += 1
        if ti == 4:
            if tj == 4:
                if not (rj <= li or ri <= lj):
                    res += 1
print(res)
