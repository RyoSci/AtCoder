h, w, k = map(int, input().split())
s = [input() for _ in range(h)]
ans = [["" for i in range(w)] for j in range(h)]


def count():
    global counter
    is_first = True
    counter += 1
    for j in range(w):
        if s[i][j] == ".":
            ans[i][j] = counter
        else:
            if is_first:
                is_first = False
            else:
                counter += 1
            ans[i][j] = counter


def check_blank():
    for _ in range(w):
        if s[i][_] == "#":
            return True
    else:
        return False


counter = 0

for i in range(h):
    if check_blank():
        start_i = i
        count()
        break

for i in range(start_i - 1, -1, -1):
    if not check_blank():
        ans[i] = ans[i + 1]
    else:
        count()

for i in range(start_i + 1, h, 1):
    if not check_blank():
        ans[i] = ans[i - 1]
    else:
        count()

for i in range(h):
    print(*ans[i])
