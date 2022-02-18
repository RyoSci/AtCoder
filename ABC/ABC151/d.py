from queue import Queue
h, w = map(int, input().split())
s = [input() for _ in range(h)]

ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            q = Queue()
            num = 0
            passed = set()
            passed.add((i, j))
            q.put([(i, j), num])
            while not q.empty():
                (i, j), num = q.get()
                i_ = []
                j_ = []
                if i - 1 >= 0:
                    i_.append(i - 1)
                    j_.append(j)
                if i + 1 <= h - 1:
                    i_.append(i + 1)
                    j_.append(j)
                if j - 1 >= 0:
                    i_.append(i)
                    j_.append(j - 1)
                if j + 1 <= w - 1:
                    i_.append(i)
                    j_.append(j + 1)
                for k in range(len(i_)):
                    if s[i_[k]][j_[k]] == "." and (i_[k], j_[k]) not in passed:
                        passed.add((i_[k], j_[k]))
                        q.put([(i_[k], j_[k]), num + 1])
                        ans = max(ans, num + 1)

print(ans)
