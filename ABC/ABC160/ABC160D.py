import numpy as np
n,x,y=map(int,input().split())
array=[]
for i in range(1,n):
    # tmp=[]
    for j in range(i+1,n+1):
        array.append(min(abs(j-i),abs(x-j)+1+abs(y-i),abs(y-j)+1+abs(x-i)))
    # if i<x:
    #     for j in range(i+1,n+1):
    #         if j<=x:
    #             tmp.append(j-i)
    #         elif x<j and j<y:
    #             tmp.append(min(j-i,abs(j-y)+1+x-i))
    #         elif y<=j:
    #             tmp.append(j-y+1+x-i)
    # elif x<=i and i<=y:
    #     for j in range(i+1,n+1):
    #         if j<=x:
    #             tmp.append(j-i)
    #         elif x<j and j<y:
    #             tmp.append(min(j-i,abs(j-y)+1+x-i))
    #         elif y<=j:
    #             tmp.append(j-y+1+x-i)
    # elif y<i:
    #     for j in range(i+1,n+1):
    #         if j<=x:
    #             tmp.append(j-i)
    #         elif x<j and j<y:
    #             tmp.append(min(j-i,abs(j-y)+1+x-i))
    #         elif y<=j:
    #             tmp.append(j-y+1+x-i)
    # array.append(tmp)
array=np.array(array)
for i in range(1,n):
    print(np.sum(array==i))
#########################################################
import numpy as np
n,x,y=map(int,input().split())
array=[]
for i in range(1,n):
    # tmp=[]
    for j in range(i+1,n+1):
        array.append(min(abs(j-i),abs(x-j)+1+abs(y-i),abs(y-j)+1+abs(x-i)))
        if i<x:
            for j in range(i+1,n+1):
                if j<=x:
                    tmp.append(j-i)
                elif x<j and j<y:
                    tmp.append(min(j-i,abs(j-y)+1+x-i))
                elif y<=j:
                    tmp.append(j-y+1+x-i)
        elif x<=i and i<=y:
            for j in range(i+1,n+1):
                array.append(min(abs(j-i),abs(x-j)+1+abs(y-i),abs(y-j)+1+abs(x-i)))
        elif y<i:
            for j in range(i+1,n+1):
                if j<=x:
                    tmp.append(j-y+1+x-i)
                elif x<j and j<y:
                    tmp.append(min(j-i,abs(j-x)+1+abs(y-i)))
                elif y<=j:
                    tmp.append(j-i)
array=np.array(array)
for i in range(1,n):
    print(np.sum(array==i))
#########################################################
# import numpy as np
n,x,y=map(int,input().split())
# array=[0 for i in range(n)]
array=[None]*n
for i in range(n):
    array[i]=0
for i in range(1,n):
    for j in range(i+1,n+1):
        res=min(abs(j-i),abs(x-j)+1+abs(y-i),abs(y-j)+1+abs(x-i))
        array[res]+=1
for i in range(1,n):
    print(array[i])

