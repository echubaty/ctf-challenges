#!/usr/bin/python

new_file = open("ext-super-magic-fixed.img", "wb")

with open("ext-super-magic.img", "rb") as file:
	data = file.read()

	# ext2 filesystem has 53ef as the magic number at position 1080-1081, fix the corrupted image here
	new_file.write(data[:1080] + bytearray.fromhex("53ef") + data[1082:])

new_file.close()
