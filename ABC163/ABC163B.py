day,work_num=map(int,input().split())
works=list(map(int,input().split()))
if day>=sum(works):
    print(day-sum(works))
else:
    print(-1)
