#!/usr/bin/python

from pwn import *
import re
import binascii

def you_shall_receive():
	response = r.recv(1000)
	log.info(response)
	return response

def do_the_send(remote, message):
	remote.send(str(message) + "\n")
	time.sleep(3)

r = remote('2018shell.picoctf.com', 64706)

response = you_shall_receive()

# Give binary string as ascii
bin_regex = re.compile(r"\b[01]+\b")
match = bin_regex.findall(response)

n = int('0b' + ''.join(match), 2)
text = binascii.unhexlify('%x' % n)
do_the_send(r, text)

response = you_shall_receive()

# Give hex string as ascii
hex_regex = re.compile(r"\b[0-9a-f]+\b")
match = hex_regex.findall(response)

text = (''.join(match)[:-1]).decode("hex")
do_the_send(r, text)

response = you_shall_receive()

# Give dec string as ascii
dec_regex = re.compile(r"\b[\d]+\b")
match = dec_regex.findall(response)

text = ''.join([chr(int(x, 8)) for x in match])
print(text)

do_the_send(r, text)

response = you_shall_receive()


# r.interactive()
