x=int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors
x_yakusuu=list(make_divisors(x))
flag=True
for l in x_yakusuu:
    r=x//l
    for b in range(10**6):
        if (b+l)**4+b*(b+l)**3+((b+l)**2)*b**2+(b+l)*b**3+b**4==r:
            a=b+l
            flag=False
            break
        b=-b
        if (b+l)**4+b*(b+l)**3+((b+l)**2)*b**2+(b+l)*b**3+b**4==r:
            a=b+l
            flag=False
            break
    if flag:
        break
    l=-l
    r=-r
    for b in range(10**6):
        if (b+l)**4+b*(b+l)**3+((b+l)**2)*b**2+(b+l)*b**3+b**4==r:
            a=b+l
            flag=False
            break
        b=-b
        if (b+l)**4+b*(b+l)**3+((b+l)**2)*b**2+(b+l)*b**3+b**4==r:
            a=b+l
            flag=False
            break
    if flag:
        break
print(a,b)