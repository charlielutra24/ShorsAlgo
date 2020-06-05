def find_gcf(a, b):
    while a != b:
        if a > b:
            a -= b
        elif b > a:
            b -= a
    return a
