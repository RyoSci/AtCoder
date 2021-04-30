s = input()
mark_10_to_14 = [[0 for j in range(5)] for i in range(4)]

q = []
mark = -1
for i in s:
    if mark == -1:
        for mark, j in enumerate("SHDC"):
            if i == j:
                break
    else:
        if i == "1":
            continue

        for num, k in enumerate(["2", "3", "4", "5", "6", "7", "8", "9", "0", "J", "Q", "K", "A"]):
            if i == k:
                break

        if k == "0":
            k = "1" + k
        q.append(j + k)
        if k in ["10", "J", "Q", "K", "A"]:
            mark_10_to_14[mark][num-8] = 1

        for l in range(4):
            tmp = 1
            for m in mark_10_to_14[l]:
                tmp *= m
            if tmp == 1:
                break
        if tmp == 1:
            break
        mark = -1

ans = ""
for i in q:
    for k in ["10", "J", "Q", "K", "A"]:
        if i == j + k:
            break
    else:
        ans += i
if ans == "":
    ans = 0

print(ans)
