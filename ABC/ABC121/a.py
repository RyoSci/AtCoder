H, W = map(int, input().split())
h, w = map(int, input().split())

res = max(0, H - h) * max(0, W - w)
print(res)