import numpy as np
import copy
n=int(input())

n_n=[[[n*i+j] for j in range(n)] for i in range(n)]
n_n_t=[[[n*i+j] for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        n_n[i][j]=n*i+j
        n_n_t[j][i]=n*i+j

n_n=np.array(n_n)
n_n_t=np.array(n_n_t)


# print(n_n)
# print(n_n_t)

q=int(input())

tenchi_or_not=0
for i in range(q):
    line=input()
    if line[0]=="3":
        tenchi_or_not+=1
        n_n.T
    else:
        num,a,b=map(int,line.split())
        if num==4:
            print(n_n[a-1][b-1])
            # if tenchi_or_not%2==0:
            #     print(n_n[a-1][b-1])
            # else:
            #     print(n_n_t[a-1][b-1])
        elif num==1:
            tmp=copy.deepcopy(n_n[a-1])
            n_n[a-1]=copy.deepcopy(n_n[b-1])
            n_n[b-1]=tmp

            # tmp=n_n_t[a-1].copy()
            # n_n_t[a-1]=n_n_t[b-1].copy()
            # n_n_t[b-1]=tmp
        elif num==2:
            tmp=copy.deepcopy(n_n[:,a-1:a])
            n_n[:,a-1:a]=copy.deepcopy(n_n[:,b-1:b].copy())
            n_n[:,b-1:b]=tmp

            # tmp=n_n_t[:,a-1:a].copy()
            # n_n_t[:,a-1:a]=n_n_t[:,b-1:b].copy()
            # n_n_t[:,b-1:b]=tmp