#これは大嘘！！！ min_mod * min_mod+1 が最小にならない可能性もある！！！
l ,r = map(int, input().split())
if l % 2019 + (r - l) >= 2019:
    print(0)
else:
    print(((l % 2019) * ((l + 1) % 2019)) % 2019)