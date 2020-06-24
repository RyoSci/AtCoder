a=int(input())
counter=0
for i in range(a+1):
    if i%15==0 or i%3==0 or i%5==0:
        continue
    else:
        counter+=i
print(counter)