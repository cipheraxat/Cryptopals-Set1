def xor(b1, b2):
    b = bytearray(len(b1))
    for i in range(len(b1)):
        b[i] = b1[i] ^ b2[i]
    return b

b1 = bytearray.fromhex("1c0111001f010100061a024b53535009181c")
b2 = bytearray.fromhex("686974207468652062756c6c277320657965")

b = bytes(xor(b1, b2))

b = b.encode("hex")

print b

