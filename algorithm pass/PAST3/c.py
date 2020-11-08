syokou,kouhi,nkou=map(int,input().split())
res=syokou

for i in range(nkou-1):
    res*=kouhi

    if res>10**9:
        print("large")
        break
else:
    print(res)