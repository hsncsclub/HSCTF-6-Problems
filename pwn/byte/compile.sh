#!/bin/sh

rm -rf bin
mkdir -p bin

gcc byte.c -o byte -m32 -fPIE -pie -O0 -Wl,-z,relro -g0 -fstack-protector
echo 'hsctf{l0l-opt1mizati0ns_ar3-disabl3d}' > flag

mv flag byte bin/
