a, b, c = map(int, input().split())
abc = [[a, "A"], [b, "B"], [c, "C"]]
abc.sort()
print(abc[1][1])
