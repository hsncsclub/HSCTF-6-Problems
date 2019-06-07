# coding=utf8

chars = dict(zip(
    u"𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣",
    u"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
))

with open("reversed.txt", "rb") as inp:
    contents = inp.read()

decoded = contents[::-1].decode("utf8")[::-1]

plain = "".join(chars.get(i, i) for i in decoded)

flag_index = plain.index("hsctf{")
print(plain[flag_index:plain.index("}", flag_index) + 1])
