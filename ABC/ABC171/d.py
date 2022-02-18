n=int(input())
a=list(map(int,input().split()))
q=int(input())
nums=[0]*10**5
for i in a:
    nums[i-1]+=1
res=sum(a)
# print(nums)
for i in range(q):
    b,c=map(int,input().split())
    res-=(b)*nums[b-1]
    res+=(c)*nums[b-1]
    nums[c-1]+=nums[b-1]
    nums[b-1]=0
    print(res)
