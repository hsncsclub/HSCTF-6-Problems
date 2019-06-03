#!/bin/sh

rm -rf bin
mkdir -p bin

gcc byte.c -o byte -m32 -fPIE -pie -O0 -Wl,-z,relro,-z,now -g0 -fstack-protector
echo 'HSCTF{l0l-opt1mizati0ns_ar3-disabl3d}' > flag

mv flag byte bin/
