# Adapted from https://gist.github.com/elliptic-shiho/e76e7c2a2aff228d7807

# This implements theorem 5.8 of
# https://people.cs.nctu.edu.tw/~rjchen/ECC2012S/Elliptic%20Curves%20Number%20Theory%20And%20Cryptography%202n.pdf
p = 0xb09700d3d1c7123f0b0336474c18c3f3f60002d480a4bce33f007c08b498197ed832687c47c2bc76b7eb199d3a420fcf77d3e5a32389fefb1032744bb473a4bd
A = 0x1b2a886d1cfcaecd03954657956cd03df56ec7709fbb0de738fb073ed20b92b6fa3d72f771618c5e2060a23c33b586a6046993894fd4950db2c12776e77fdbd1
B = 0x303bde5e945d46949b8c9986519a9a1f0301f61ff043b3bf2785fd85e365e4caa163c64ad307db8dbbac0087fd8562273ee61aac095815030cc73c7495b46ddb

E = EllipticCurve(GF(p), [A, B])

print E.order() == p

g = E(0x9f12acd5b74cc67e03506be8f904087863ce7fd8ed1de6404f26e8e96bea3761fca1f5b21def5298e7adbbf8787ea431a43d241fda6bc9fbaddeaff35ab4f7c3, 0x51f33f0e5c36e1bf91ac78b04c7e4f819bfad8db291fc2e20c10ee00e98525927719ecf0e8b96c5e62e3f48a38b94e72dddee1109bfdad9c7dfd3f566da69eb4)
v = E(1177058043549358413014554258002815119079001682731148396776662750875463733619059415667987598866208023692880799135159888362631239206873676420277546691755222, 6042132606876152754155047441818131810928517366269481359146510190883638121779596002132009344517568983680414721512960291321687246617263491498797986759689315)

def hensel_lift(point):
    x,y = map(long, point.xy())
    fr = y**2 - (x**3 + A*x + B)
    # t = (-fr / p) / f'
    # f'= 2y
    t = (((- fr / p) % p) * inverse_mod(2*y, p)) % p
    lifted_y = y + p * t
    return x, lifted_y

x1, y1 = hensel_lift(g)
x2, y2 = hensel_lift(v)

# Now we take a lift of E, and it will be mod p^2
# A lift of E just means a curve that contains the lifts of g and v,
# and reduces to E mod p

A2 = y2**2 - y1**2 - (x2**3 - x1**3)
A2 = A2 * inverse_mod(x2 - x1, p^2)
A2 %= p^2

B2 = y1**2 - x1**3 - A2 * x1
B2 %= p^2

# new curve
E2 = EllipticCurve(IntegerModRing(p^2), [A2, B2])

# calculate dlog
# We use the ideas of Lawrence C. Washington's Elliptic curves (Theorem 5.8)
# We multiply by (p - 1) so the denominators don't have a factor of p, since if it did, we can't invert by it.
g2 = (p - 1) * E2(x1, y1)
v2 = (p - 1) * E2(x2, y2)

g2x, g2y = map(long, g2.xy())
v2x, v2y = map(long, v2.xy())

# The factors of p in computation of m1 and m2 are divided out of the x terms before inversion

m1 = (g2y - y1) * inverse_mod(((g2x - x1) / p) % p, p)
m2 = (v2y - y2) * inverse_mod(((v2x - x2) / p) % p, p)

dlog = (m1 * inverse_mod(m2, p)) % p

print dlog

assert g * dlog == v

# Boring stuff for problem

bob_pub_x = 0x993cf91c25dd287e30cb8f6a0d4fa70e89e90ac0953e7ee876b1ef190a6a442235479162b5ac61beb1d1a5aca03313ff5c53c2e3c81df2fbedf3b0add0b20d18
bob_pub_y = 0x4e75b39de8d5daa3f5f489c02b8fa2cce6f2cfb406bb4a5a0d75d29a3021dcd61df697ef485743e7f8a1b9cc60879bc808e74f9c909b2f0cecb1df0a03c771f5

bobPubKey = E(bob_pub_x, bob_pub_y)
DH_secret = dlog * bobPubKey

from hashlib import sha256
from Crypto.Cipher import AES
AES_secret = sha256(str(DH_secret.xy())).digest()
obj = AES.new(AES_secret, AES.MODE_ECB)

import binascii
ciphertext = binascii.unhexlify("d5cb4f93aa95af738bbcf5cbc1d4f1b66c9c9f84b4257035cf19e3ee41e2b79384fed7ef7d9fb58f6dfb86fefc95429b9f87b5b8a330aa082681fd140b8156bd")
print obj.decrypt(ciphertext)