n = int(input())
for i in range(100, 1000):
    tmp = str(i) 
    if len(set(tmp)) == 1 and i >= n:
        print(i)
        break