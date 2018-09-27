# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 01:19:01 2018

@author: Admin
"""

from Crypto.Cipher import AES

obj = AES.new("YELLOW SUBMARINE", AES.MODE_ECB)

ciphertext = "".join(list(open("7.txt", "r"))).decode("base64")
plaintext = obj.decrypt(ciphertext)
print plaintext