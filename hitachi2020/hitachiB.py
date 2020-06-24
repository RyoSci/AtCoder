a,b,m=map(int,input().split())
a_prices=[int(i) for i in input().split()]
b_prices=[int(i) for i in input().split()]
a_min=min(a_prices)
b_min=min(b_prices)
a_add_b=a_min+b_min
for i in range(m):
    x,y,c=map(int,input().split())
    if a_prices[x-1]+b_prices[y-1]-c<a_add_b:
        a_add_b=a_prices[x-1]+b_prices[y-1]-c
print(a_add_b)