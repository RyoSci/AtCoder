n = int(input())
w = input().split()
alphabet2num = dict()
alphabet2num = {
    "b": 1, "c": 1, "d": 2, "w": 2, "t": 3, "j": 3, "f": 4, "q": 4, "l": 5, "v": 5, "s": 6, "x": 6, "p": 7, "m": 7, "h": 8, "k": 8, "n": 9, "g": 9, "z": 0, "r": 0
}

ans = [""] * n
for i in range(n):
    for j in w[i]:
        j = j.lower()
        if j not in alphabet2num:
            continue
        ans[i] += str(alphabet2num[j])

res = []
for i in range(n):
    if ans[i] == "":
        continue
    res.append(ans[i])

print(*res)
