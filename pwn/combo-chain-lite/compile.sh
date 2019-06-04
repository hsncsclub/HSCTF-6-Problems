#!/bin/sh

rm -r bin

gcc combo-chain-lite.c -o combo-chain-lite -no-pie -g0 -fno-stack-protector
echo 'hsctf{wheeeeeee_that_was_fun}' > flag

mkdir -p bin
mv flag combo-chain-lite bin/
cp combo-chain-lite.c bin/
