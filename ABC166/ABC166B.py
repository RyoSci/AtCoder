n_nin,okasi=map(int,input().split())
okasi_have=[0]*n_nin
for i in range(1,okasi+1):
    di=int(input())
    ai_list=list(map(int,input().split()))
    for j in ai_list:
        okasi_have[j-1]+=1
    
print(okasi_have.count(0))
    