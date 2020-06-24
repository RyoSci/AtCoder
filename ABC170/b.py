x,y=map(int,input().split())

flag=False
for i in range(0,101):
    for j in range(0,101):
        if i+j==x and i*2+j*4==y:
            flag=True
            break
if flag:
    print("Yes")
else:
    print("No")