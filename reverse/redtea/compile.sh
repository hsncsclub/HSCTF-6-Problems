#!/bin/sh

rm bin/flag.txt bin/redtea
mkdir -p bin

gcc redtea.c -o redtea -Wall -m32 -fPIE -pie -Os -Wl,-z,relro,-z,now -g0 -fstack-protector
echo 'HSCTF{rob_made_jess_a_cup_of_tea_wink_wink_101}' > flag.txt

mv flag.txt redtea bin/
