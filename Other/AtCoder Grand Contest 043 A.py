import numpy as np
import copy as cp
h,w=map(int,input().split())
table=[[i for i in input()]for j in range(h)]
table=np.array(table)

def good_or_bad(array,h,w):
    x=1
    y=1
    table_copy=cp.deepcopy(array)
    right_or_down=0
    if table_copy[1][1]=="#":
        return False

    while x!=h and y!=w:
        if table_copy[x-1][y-1]==".":
            if right_or_down%2==0:
                y+=1
            else:
                x+=1
        else:
            if right_or_down%2==0:
                y-=1
            else:
                x-=1
            right_or_down+=1    
    else:
        print(0)

table_copy=cp.deepcopy(table)
for i in range(h):
    for j in range(h):
        for k in range(w):
            for l in range(w):
                
                table_copy[i:j,k:l]="."

                
good_or_bad(table,h,w)