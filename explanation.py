# g = a random (smallish) number
# N = the large number we want to factorise
done = False
while not done:
    # Each iteration, raise g to the next power p.

    # Eventually g^p = (some integer m * N) + 1.
    # So our eventual goal is to find the value of p needed for this to be true.
    # We can then use Euclid's algorithm to find the common factor of (g^p -1) and (mN)
    #       which should be a factor of N.

    # So m * N = g^p - 1 = (g^(p/2)+1) * (g^(p/2)-1)

    # Now there are three possibilities:
    # 1. p is not an even number.
    # 2. One of g^(p/2)+1 and g^(p/2)-1 is a multiple of N itself, and the other is just a factor of m.
    # For these possibilities, we cannot find a factor of N, so we pick a new value for g and start over.
    # 3. Each of g^(p/2)+1 and g^(p/2)-1 is a multiple of the two factors of N.
    # This is the outcome we want. This occurs roughly 3/8 of the time.
    # We then use Euclid's algorithm to find:
    # GCF of N and g^(p/2)+1 for one factor of N,
    # GCF of N and g^(p/2)-1 for the other factor of N.
    pass


