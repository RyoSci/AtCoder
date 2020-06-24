a,v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())

if a==b:
    print("YES")
else:
    if w>=v:
        print("NO")
    else:
        if  abs(a-b)/(v-w)<=t:
            print("YES")
        else:
            print("NO")