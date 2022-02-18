n = int(input())
w = list(input().split())
ego = ["TAKAHASHIKUN", "Takahashikun", "takahashikun"]
res = 0
for i in w:
    for j in ego:
        if i[-1] == ".":
            i = i[:-1]
        if i == j:
            res += 1

print(res)
