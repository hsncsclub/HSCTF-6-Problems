#!/bin/sh

rm -r bin

gcc bit.c -o bit -m32 -no-pie -g0 
echo 'hsctf{flippin_pwn_g0d}' > flag

mkdir -p bin
mv flag bit bin/