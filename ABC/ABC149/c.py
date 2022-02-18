x = int(input())

def judge_prime_number(x):
    for i in range(2, int(x ** (1/2)) + 1):
        if x % i == 0:
            return False
    else:
        return True

while True:
    if not judge_prime_number(x):
        x += 1
        continue
    else:
        print(x)
        break