import subprocess
import random

while True:
    n0 = random.randint(1, 3)
    n1 = random.randint(1, 3)
    n2 = random.randint(1, 3)

    s = [""]*3
    for i, ni in zip(range(3), [n0, n1, n2]):
        for j in range(ni):
            tmp = random.randint(0, 25)
            s[i] += chr(tmp+ord("a"))

    diff0 = subprocess.run(
        f"python diff0.py {s[0]} {s[1]} {s[2]}", shell=True, stdout=subprocess.PIPE)
    diff1 = subprocess.run(
        f"python diff1.py {s[0]} {s[1]} {s[2]}", shell=True, stdout=subprocess.PIPE)

    if diff0.stdout != diff1.stdout:
        print(diff0.stdout)
        print(diff1.stdout)
        print(s, sep="`\n")
        break
