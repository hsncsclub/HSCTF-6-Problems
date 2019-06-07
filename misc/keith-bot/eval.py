import os
import pwd
import sys
import textwrap

pw = pwd.getpwnam("nobody")

os.chdir("home")
os.chroot(".")

os.setgroups(())
os.setgid(pw.pw_gid)
os.setuid(pw.pw_uid)

env = {"__builtins__": {}}

exec(f"def func():\n{textwrap.indent(sys.stdin.read(), '    ')}", env)

ret = env["func"]()

if ret is not None:
    print(ret)
