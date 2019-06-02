import random as r

flag_arr = [ord(c) for c in 'hsctf{wH04_u_r_2_pr0_4_th1$}']

for i in range(len(flag_arr)):
    print 'L' + str(i) + ':'
    print '        dup'
    if (i <= 5):
        print '        iconst_' + str(i)
    else:
        print '        bipush ' + str(i)

    print '        caload'
    
    xor_key = r.randint(-0xFFFFFFF, 0xFFFFFFF)
    xor_thing = xor_key ^ flag_arr[i]
    
    print '        ldc ' + str(xor_key)
    print '        ixor'
    print '        ldc ' + str(xor_thing)
    print '        isub'
    if (len(flag_arr) - 1 == i):
        print '        ifeq Lgood'
    else:
        print '        ifeq L' + str(i + 1)
    print '        pop'
    print 'LA' + str(i) + ':'
    print '        iload_2'
    print '        ifne LA' + str(r.randint(0, 26))
    print '        jsr Lfail'

print '        return' # otherwise jvm gets mad about "illegal class"
input()