#!/bin/sh

mkdir -p bin


gcc bit.c -o bit -m32 -no-pie -g0 
echo 'HSCTF{flippin_pwn_g0d}' > flag

mv flag bit bin/
