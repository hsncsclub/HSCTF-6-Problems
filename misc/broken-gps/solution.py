flag = "hsctf{"

for i in range(1, 13):
    with open("input/%d.txt" % i) as inp_file:
        inp = inp_file.read()
        flag += chr(97 + int(0.5 + 2 * ((inp.count("east") - inp.count("west")) ** 2 + (inp.count("north") - inp.count("south")) ** 2) ** 0.5) % 26)

flag += "}"

print(flag)
