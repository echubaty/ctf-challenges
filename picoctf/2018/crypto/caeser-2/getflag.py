#!/usr/bin/python

with open('ciphertext', 'r') as f:
	cipher = f.read()

for i in range(255):
	brute = []

	for x in cipher:

		if (ord(x) + i) % 255 < 159 or (ord(x) + i) % 255 > 185:
			brute.append(chr((ord(x) + i) % 255))
		else:
			# Weird hack, the uppercase letters weren't decrypting properly
			brute.append(chr((ord(x) + i - 159 + ord('A')) % 255))


	brute = ''.join(brute)

	if 'pico' in brute:
		print(brute[:-1])
