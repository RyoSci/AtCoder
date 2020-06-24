import math
a,b,h,m=map(int,input().split())
alpha=math.pi*m/30
beta=math.pi*(h*60+m)/360

if alpha>beta:
    sita=alpha-beta
else:
    sita=beta-alpha

sita=min(sita,2*math.pi-sita)

c=(a**2+b**2-2*a*b*math.cos(sita))**(1/2)
print(c)