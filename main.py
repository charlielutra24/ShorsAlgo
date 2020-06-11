import random
from euclid_algo import find_gcf
# To save memory, since higher values of g make for much larger numbers, I will use g=2,3,4 etc.
g = 2
N = 217
done = False
p = 0
p_values = []
while not done:
    p += 1
    r = g**p % N
    if g**p % N == 1:
        print(g, p)
        p_values.append(p)
    if len(p_values) >= 1:
        p = p_values[0]
        if p_values[0] % 2 != 0:
            g += 1
            p = 0
            p_values = []
        else:
            x = g**(p/2)+1
            y = g**(p/2)-1
            a = int(find_gcf(N, x))
            b = int(find_gcf(N, y))
            if a == 1 or b == 1:
                g += 1
                p = 0
                p_values = []
            else:
                print(g, p, a, b)
                done = True
    if p > 500:
        g += 1
        p = 0
        p_values = []

print(a, "x", b, "=", N)
