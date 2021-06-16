x = int(input())

for i in range(10**6):
    if x <= i*(i+1)//2:
        print(i)
        exit()
