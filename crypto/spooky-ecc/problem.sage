p = 0xb09700d3d1c7123f0b0336474c18c3f3f60002d480a4bce33f007c08b498197ed832687c47c2bc76b7eb199d3a420fcf77d3e5a32389fefb1032744bb473a4bd
A = 0x1b2a886d1cfcaecd03954657956cd03df56ec7709fbb0de738fb073ed20b92b6fa3d72f771618c5e2060a23c33b586a6046993894fd4950db2c12776e77fdbd1
B = 0x303bde5e945d46949b8c9986519a9a1f0301f61ff043b3bf2785fd85e365e4caa163c64ad307db8dbbac0087fd8562273ee61aac095815030cc73c7495b46ddb
g_x = 0x9f12acd5b74cc67e03506be8f904087863ce7fd8ed1de6404f26e8e96bea3761fca1f5b21def5298e7adbbf8787ea431a43d241fda6bc9fbaddeaff35ab4f7c3
g_y = 0x51f33f0e5c36e1bf91ac78b04c7e4f819bfad8db291fc2e20c10ee00e98525927719ecf0e8b96c5e62e3f48a38b94e72dddee1109bfdad9c7dfd3f566da69eb4

E = EllipticCurve(GF(p), [A, B])
g = E(g_x, g_y)

def generateKey():
    private = randint(1, E.order() - 1)
    public = g * private

    return(public, private)

def computeSharedSecret(pubkey, privkey):
    return pubkey * privkey

def secure_send_flag():
    from secret import flag
    myPubKey, myPrivKey = generateKey()

    print myPubKey

    bob_pub_x = 0x993cf91c25dd287e30cb8f6a0d4fa70e89e90ac0953e7ee876b1ef190a6a442235479162b5ac61beb1d1a5aca03313ff5c53c2e3c81df2fbedf3b0add0b20d18
    bob_pub_y = 0x4e75b39de8d5daa3f5f489c02b8fa2cce6f2cfb406bb4a5a0d75d29a3021dcd61df697ef485743e7f8a1b9cc60879bc808e74f9c909b2f0cecb1df0a03c771f5

    bobPubKey = E(bob_pub_x, bob_pub_y)
    DH_secret = computeSharedSecret(bobPubKey, myPrivKey)
    from hashlib import sha256
    from Crypto.Cipher import AES
    AES_secret = sha256(str(DH_secret.xy())).digest()
    obj = AES.new(AES_secret, AES.MODE_ECB)
    flag += " " * ((16 - len(flag)) % 16)
    ciphertext = obj.encrypt(flag)

