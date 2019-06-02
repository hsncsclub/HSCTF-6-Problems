#!/usr/bin/env python2

import requests
import os
import os.path

xinetd = """
service ctf
{{
    disable = no
    socket_type = stream
    protocol    = tcp
    wait        = no
    user        = root
    type        = UNLISTED
    port        = 9999
    bind        = 0.0.0.0
    server      = /usr/sbin/chroot
    # replace helloworld to your program
    server_args = --userspec=1000:1000 /home/ctf ./{}
    banner_fail = /etc/banner_fail
    # safety options
    per_source	= 10 # the maximum instances of this service per source IP address
    rlimit_cpu	= 20 # the maximum number of CPU seconds that the service may use
    #rlimit_as  = 1024M # the Address Space resource limit for the service
}}
"""

name = raw_input("What is the name of your problem? (All lowercase please): ")
path = "pwn/{}".format(name)

try:
    os.mkdir(path, 0755)
except OSError:
    if not os.path.isdir(path):
        raise

r = requests.get("https://raw.githubusercontent.com/Eadom/ctf_xinetd/master/Dockerfile", allow_redirects=True)
open(path + "/Dockerfile".format(name), 'wb').write(r.content)

r = requests.get("https://raw.githubusercontent.com/Eadom/ctf_xinetd/master/start.sh", allow_redirects=True)
open(path + "/start.sh".format(name), 'wb').write(r.content)

open(path + "/ctf.xinetd".format(name), 'w').write(xinetd.format(name))

try:
    os.mkdir(path + "/bin", 0755)
except OSError:
    if not os.path.isdir(path + "/bin"):
        raise

print "Done! Place your compiled binary and flag (with correct name) into pwn/{}/bin!".format(name)
