#!/bin/sh

rm -r bin

gcc return-to-sender.c -o return-to-sender -m32 -no-pie -g0 -fno-stack-protector
echo 'hsctf{fedex_dont_fail_me_now}' > flag

mkdir -p bin
mv flag return-to-sender bin/
cp return-to-sender.c bin/
