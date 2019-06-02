import random as r

flag_arr = [ord(c) for c in 'hsctf{y0u_d3f34t3d_th3_b4by_vm}']

ip = 0
for i in range(len(flag_arr)):
    xor_key = r.randint(-0xFF, 0xFF)
    xor_thing = xor_key ^ flag_arr[i]
    print '                /* ' + str(ip) + ' */ 0xb, 0x0, // push r0 (index)'
    print '                /* ' + str(ip + 2) + ' */ 0x6, ' + hex(i) + ', // push ' + hex(i)
    print '                /* ' + str(ip + 4) + ' */ 0x1, ' + hex(r.randint(-0xFF, 0xFF)) + ', // sub'
    print '                /* ' + str(ip + 6) + ' */ 0x5, ' + hex(ip + 20) + ', // if not 0, ip = ' + str(ip + 20)
    print '                /* ' + str(ip + 8) + ' */ 0xb, 0x1, // push r1 (answer)'
    print '                /* ' + str(ip + 10) + ' */ 0x6, ' + hex(xor_key) + ', // push ' + hex(xor_key)
    print '                /* ' + str(ip + 12) + ' */ 0x9, ' + hex(r.randint(-0xFF, 0xFF)) + ', // xor'
    print '                /* ' + str(ip + 14) + ' */ 0x6, ' + hex(xor_thing) + ', // push ' + hex(xor_thing)
    print '                /* ' + str(ip + 16) + ' */ 0x1, ' + hex(r.randint(-0xFF, 0xFF)) + ', // sub'
    print '                /* ' + str(ip + 18) + ' */ 0xc, ' + hex(r.randint(-0xFF, 0xFF)) + ', // kill'
    ip += 20

input()
