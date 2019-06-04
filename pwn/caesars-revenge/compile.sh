#!/bin/bash

gcc caesars-revenge.c -o bin/caesars-revenge -no-pie
echo "hsctf{should_have_left_%n_back_in_ancient_rome}" > bin/flag
