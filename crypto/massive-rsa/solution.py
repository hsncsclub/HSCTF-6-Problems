import binascii

with open("massive.txt") as massive:
    exec(massive.read())

# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm

def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

def mulinv(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, _ = xgcd(a, b)
    if g == 1:
        return x % b

m = pow(c, mulinv(e, n - 1), n)

print(binascii.unhexlify(hex(m)[2:].rstrip("L")).decode())
