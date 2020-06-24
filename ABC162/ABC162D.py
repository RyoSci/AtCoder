a=int(input())
b=input()
counter=0
for i in range(a):
    for j in range(i+1,a):
        for k in range(j+1,a):
            if b[i]!=b[j] and b[j]!=b[k] and b[k]!=b[i]:
                if j-i!=k-j:
                    counter+=1
print(counter)

a=int(input())
moji=input()
r=[]
g=[]
b=[]
for i in range(a):
    if moji[i]=="R":
        r.append(i)
    elif moji[i]=="G":
        g.append(i)
    else:
        b.append(i)
res=len(r)*len(g)*len(b)
if len(r)==0 or len(g)==0 or len(b)==0:
    print(0)
else:
    min_len={0:r,1:g,2:b}
    if len(min_len[0])>len(min_len[1]):
        tmp=min_len[0]
        min_len[0]=min_len[1]
        min_len[1]=tmp
    if len(min_len[1])>len(min_len[2]):
        tmp=min_len[1]
        min_len[1]=min_len[2]
        min_len[2]=tmp
    if len(min_len[0])>len(min_len[1]):
        tmp=min_len[0]
        min_len[0]=min_len[1]
        min_len[1]=tmp
    a1=[]
    for i in range(3):
        a1.append(min_len[i])
    I=a1[0]
    J=a1[1]
    K=a1[2]
    for i in I:
        for j in J:
            dif=abs(i-j)
            min_i_j=min(i,j)
            max_i_j=max(i,j)
            if -dif+min_i_j in K:
                res-=1
            if dif+max_i_j in K:
                res-=1
            if dif%2==0 and  dif//2+min_i_j in K:
                res-=1
    print(res)

a=int(input())
moji=input()
r=set()
g=set()
b=set()
for i in range(a):
    if moji[i]=="R":
        r.add(i)
    elif moji[i]=="G":
        g.add(i)
    else:
        b.add(i)
res=len(r)*len(g)*len(b)
if len(r)==0 or len(g)==0 or len(b)==0:
    print(0)
else:
    min_len={0:r,1:g,2:b}
    if len(min_len[0])>len(min_len[1]):
        tmp=min_len[0]
        min_len[0]=min_len[1]
        min_len[1]=tmp
    if len(min_len[1])>len(min_len[2]):
        tmp=min_len[1]
        min_len[1]=min_len[2]
        min_len[2]=tmp
    if len(min_len[0])>len(min_len[1]):
        tmp=min_len[0]
        min_len[0]=min_len[1]
        min_len[1]=tmp
    a1=[]
    for i in range(3):
        a1.append(min_len[i])
    for i in a1[0]:
      for j in a1[1]:
        if -abs(i-j)+min(i,j) in a1[2]:
          res-=1
        if abs(i-j)+max(i,j) in a1[2]:
          res-=1
        if abs(i-j)%2==0 and  int(abs(i-j)/2)+min(i,j) in a1[2]:
          res-=1
    print(res)
                
    
a=int(input())
moji=input()
r=[]
g=[]
b=[]
for i in range(a):
    if moji[i]=="R":
        r.append(i)
    elif moji[i]=="G":
        g.append(i)
    else:
        b.append(i)
res=len(r)*len(g)*len(b)
if len(r)==0 or len(g)==0 or len(b)==0:
    print(0)
else:
    min_len={0:r,1:g,2:b}
    a1=[]
    for i in range(3):
        a1.append(min_len[i])
    for i in a1[0]:
      for j in a1[1]:
        if -abs(i-j)+min(i,j) in set(a1[2]):
          res-=1
        if abs(i-j)+max(i,j) in set(a1[2]):
          res-=1
        if abs(i-j)%2==0 and  int(abs(i-j)/2)+min(i,j) in set(a1[2]):
          res-=1
    print(res)
                
    
