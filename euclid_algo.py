def find_gcf(a, b):
    if a > b:
        return find_gcf(a-b, b)
    elif a < b:
        return find_gcf(a, b-a)
    else:
        return a
