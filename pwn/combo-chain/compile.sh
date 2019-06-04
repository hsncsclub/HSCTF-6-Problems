#!/bin/sh

rm -r bin

gcc combo-chain.c -o combo-chain -no-pie -g0 -fno-stack-protector
echo 'hsctf{i_thought_konami_code_would_work_here}' > flag

mkdir -p bin
mv flag combo-chain bin/
cp combo-chain.c bin/
