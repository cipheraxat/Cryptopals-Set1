# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 16:57:05 2018

@author: Admin
"""

lines = [
    "Burning 'em, if you ain't quick and nimble\n",
    "I go crazy when I hear a cymbal",
]

text = "".join(lines)
key = bytearray("ICE" * len(text))
plaintext = bytes(xor(bytearray(text), key))
plaintext = plaintext.encode("hex")
print plaintext