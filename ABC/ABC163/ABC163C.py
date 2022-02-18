people=int(input())
id_list=list(map(int,input().split()))
josi_map={}
for i in range(people):
    josi_map[i+1]=0

for i in id_list:
    josi_map[i]+=1

for i in range(people):
    print(josi_map[i+1])