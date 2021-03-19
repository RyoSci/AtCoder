n = int(input())
rec = dict()
pre = input()
rec[pre] = 1

ans = "DRAW"
for i in range(n - 1):
    w = input()
    if pre[-1] != w[0] or w in rec:
        if i % 2 != 0:
            ans = "LOSE"
        else:
            ans = "WIN"
        break
    rec[w] = 1
    pre = w

print(ans)
