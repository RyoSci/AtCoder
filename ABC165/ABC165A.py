a=int(input())
s,e=map(int,input().split())
for i in range(s,e+1):
    if i%a==0:
        print("OK")
        break
else:
    print("NG")