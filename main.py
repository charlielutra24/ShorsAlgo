import random
from euclid_algo import find_gcf
g = 2  # To save memory, since higher values of g make for much larger numbers in memory, I will use g=2,3,4 etc.
N = 35
done = False
p = 0
p_values = []
while not done:
    p += 1
    if g**p % N == 1:
        p_values.append(p)
    if len(p_values) >= 2:
        print(p_values)
        if p_values[0] % 1 != 0:
            g += 1
            p = 0
            p_values = []
        else:
            print("HIII!")
            a = find_gcf(N, g**(p/2)+1)
            b = find_gcf(N, g**(p/2)-1)
            if a == 1 or b == 1:
                print("HELLO")
                g += 1
                p = 0
                p_values = []
            else:
                print("hello!")
                print(g, p, a, b)
                done = True
