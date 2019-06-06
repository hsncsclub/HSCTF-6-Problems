#!/bin/sh

rm bin/flag.txt bin/redtea
mkdir -p bin

gcc redtea.c -o redtea -Wall -m32 -no-pie -Os -Wl,-z,relro,-z,now -g0 -fstack-protector
# strip redtea
echo 'hsctf{rob_made_some1_special_a_cup_of_tea_wink_wink_101}' > flag.txt

cp words.txt flag.txt redtea bin/
