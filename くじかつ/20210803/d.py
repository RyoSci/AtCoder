n, k = map(int, input().split())
d = set(map(int, input().split()))

for i in range(10**5):
    if i >= n:
        i = str(i)
        flag = True
        for j in i:
            if int(j) in d:
                flag = False
                break
        if flag:
            print(i)
            exit()
