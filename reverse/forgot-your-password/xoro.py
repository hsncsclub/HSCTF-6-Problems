#!/usr/bin/env python2

bit64 = 0xffffffffffffffff
s = [0,0]

def rotl(x, k):
	return (x << k) | (x >> (64 - k))

def rotr(x, k):
	return (x >> k) | (x << (64 - k))

def next():
	s0 = s[0]
	s1 = s[1]
	res = (s0 + s1) & bit64

	s1 ^= s0
	s[0] = rotl(s0, 55) ^ s1 ^ (s1 << 14)
	s[1] = rotl(s1, 36)
	s[0] &= bit64
	s[1] &= bit64
	return res & bit64

def prev():
	s1 = rotr(s[1], 36)
	ab = s1 ^ s[0]
	b = s1 << 14
	a = ab ^ b

	s1 &= bit64
	ab &= bit64
	b &= bit64
	a &= bit64

	s[0] = rotr(a, 55)
	s[1] = s[0] ^ s1
	s[0] &= bit64
	s[1] &= bit64
	return (s[0] + s[1]) & bit64

def bin2chr(data):
    result = ''

    while data:
        char = data & 0xff
        result += chr(char)
        data >>= 8

    return result


# run 0x7373696674637368 0x776f776c6f6f636f through xoroshiftall.py

# three before:
# s = [0x653b6c98b20cda04, 0xe3eada0c00c5e10f]

# two before:
# s = [0x1b6b2379701afd53, 0xd49942dc5d5b728d]

# one before: 
# s = [0xe2d36a8db96d9ff3, 0xd2818f22a0e62880]

s = [0xf919b487ed2f9ead, 0x7a59b4de8733d4bb]

# prev()
# prev()
# prev()
# prev()
# prev()
# prev()
# print hex(s[0]), hex(s[1])

# would print 'hsctfissocoolwow'
print(repr(''.join(bin2chr(next()) for i in range(4))))


# expected:
# Thanks! Your numbers are: 
# e06f76cd556604f0f21c34f1519d2fd2
# 73c8535ab0f954b5ad1cbab7abc18309
# hsctfissocoolwow

