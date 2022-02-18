n = int(input())
def is_prime(n):
    for i in range(2, int((n)**(1 / 2)) + 1):
        if n % i == 0:
            return False
    else:
        return True

ans = "Not Prime"
if n == 1:
    ans = "Not Prime"
elif is_prime(n):
    ans = "Prime"
else:
    sum_digits = 0
    for i in str(n):
        sum_digits += int(i)
    if n % 10 != 5 and n % 2 == 1 and sum_digits % 3 != 0:
        ans = "Prime"

print(ans)