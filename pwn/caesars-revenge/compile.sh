#!/bin/bash

gcc -fno-stack-protector caesars-revenge.c -o bin/caesars-revenge
echo "hsctf{shoulda_left_format_string_back_in_the_roman_empire}" > bin/flag
