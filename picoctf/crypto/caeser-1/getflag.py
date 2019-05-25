#!/usr/bin/python

import string
import itertools

lowercase = string.ascii_lowercase

# Modified from an assignment from COMP4140 I did previously
def decrypt_shift_cipher(ciphertext, key):
	# Use a string translation table to "shift" the characters with the found key
	return ciphertext.translate(string.maketrans(lowercase[key:] + lowercase[:key], lowercase))

cipher = "payzgmuujurjigkygxiovnkxlcgihubb"

for i in range(26):
	if i == 6: # Found via inspection
		print("picoCTF{" + decrypt_shift_cipher(cipher, i) + "}")
		