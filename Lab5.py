from math import ceil, sqrt


def BSGS(g, b, p):
    '''
    Solve for x in b = g^x mod p given a prime p.
    If p is not prime, you shouldn't use BSGS anyway.
    '''
    num = ceil(sqrt(p))
    t = {pow(g, i, p): i for i in range(num)}
    c = pow(g, num * (p - 2), p)
    for i in range(num):
        y = (b * pow(c, i, p)) % p
        if y in t:
            print(i)
            print(num)
            print(t[y])
            return i * num + t[y]
    return None
