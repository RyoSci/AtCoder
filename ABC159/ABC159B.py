line=input()
n=len(line)
flag=True

if line!=line[::-1]:
    flag=False
if line[0:int((n-1)/2)]!=line[0:int((n-1)/2)][::-1]:
    flag=False
if line[int((n+3)/2)-1:n]!=line[int((n+3)/2)-1:n][::-1]:
    flag=False
if flag:
    print("Yes")
else:
    print("No")