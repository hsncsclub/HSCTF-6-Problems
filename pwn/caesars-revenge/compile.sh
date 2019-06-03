#!/bin/bash

gcc caesars-revenge.c -o bin/caesars-revenge -no-pie
echo "hsctf{shoulda_left_format_string_back_in_the_roman_empire}" > bin/flag
