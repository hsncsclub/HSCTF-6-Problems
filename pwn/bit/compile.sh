#!/bin/sh

gcc bit.c -o bit -m32 -no-pie
echo 'HSCTF{flippin_pwn_g0d}' > flag.txt
