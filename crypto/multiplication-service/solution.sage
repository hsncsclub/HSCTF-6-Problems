p = 2^448 - 2^224 - 1
K = Zmod(p)
# Multiplicative generator
g = 7
# sign(0, g)
res = 311589760906266120933024602359475939134672273109563952308592541241419957528683030889669112603105306747274953585289179030081206329387359
#solution = x s.t. g^x = res mod p
primes = [2, 641, 18287, 196687, 1466449, 2916841, 6700417, 1469495262398780123809, 167773885276849215533569, 596242599987116128415063, 37414057161322375957408148834323969]
assert prod(primes) == (p - 1)
ranges = primes[:7] + [2^40, 2^40, 2^40, 2^40]
dlogs = []
for i in range(len(primes)):
    # map to subgroup
    base_n = K(pow(g, (p - 1) / primes[i], p))
    res_n = K(pow(res, (p - 1) / primes[i], p))
    dlogs += [discrete_log_lambda(res_n, base_n, (0, ranges[i]))]

dlog = CRT(dlogs, primes)
assert pow(g, dlog, p) == res
print(dlog)