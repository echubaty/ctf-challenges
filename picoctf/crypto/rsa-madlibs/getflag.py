#!/usr/bin/python

from pwn import *
import re


def you_shall_receive():
	response = r.recv(2048)
	log.info(response)
	return response

def do_the_send(remote, message):
	remote.send(str(message) + "\n")
	time.sleep(3)

# From https://rosettacode.org/wiki/Modular_inverse#Python
def extended_gcd(aa, bb):
	lastremainder, remainder = abs(aa), abs(bb)
	x, lastx, y, lasty = 0, 1, 1, 0
	while remainder:
		lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
		x, lastx = lastx - quotient*x, x
		y, lasty = lasty - quotient*y, y
	return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
 
def mod_inverse(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m


r = remote('2018shell.picoctf.com', 50430)
you_shall_receive()
response = you_shall_receive()

p_regex = re.compile("p : \d+")
q_regex = re.compile("q : \d+")
n_regex = re.compile("n : \d+")
e_regex = re.compile("e : \d+")
plaintext_regex = re.compile("plaintext : \d+")
ciphertext_regex = re.compile("ciphertext : \d+")

p = int(p_regex.search(response).group(0)[3:])
q = int(q_regex.search(response).group(0)[3:])

n = p * q

do_the_send(r, "Y")
do_the_send(r, n)


response = you_shall_receive()

p = int(p_regex.search(response).group(0)[3:])
n = int(n_regex.search(response).group(0)[3:])

q = n / p

do_the_send(r, "Y")
do_the_send(r, q)
you_shall_receive()

do_the_send(r, "N")
response = you_shall_receive()

do_the_send(r, "Y")

p = int(p_regex.search(response).group(0)[3:])
q = int(q_regex.search(response).group(0)[3:])

totient = (p - 1) * (q - 1)

do_the_send(r, totient)
response = you_shall_receive()

do_the_send(r, "Y")

e = int(e_regex.search(response).group(0)[3:])
n = int(n_regex.search(response).group(0)[3:])
plaintext = int(plaintext_regex.search(response).group(0)[12:])

ciphertext = (plaintext ** e) % n

do_the_send(r, ciphertext)
you_shall_receive()

do_the_send(r, "N")

do_the_send(r, "Y")
response = you_shall_receive()


q = int(q_regex.search(response).group(0)[3:])
p = int(p_regex.search(response).group(0)[3:])
e = int(e_regex.search(response).group(0)[3:])

totient = (p - 1) * (q - 1)

d = mod_inverse(e, totient)
do_the_send(r, d)

do_the_send(r, "Y")
response = you_shall_receive()

p = int(p_regex.search(response).group(0)[3:])
e = int(e_regex.search(response).group(0)[3:])
n = int(n_regex.search(response).group(0)[3:])
q = n / p
ciphertext = int(ciphertext_regex.search(response).group(0)[13:])

totient = (p - 1) * (q - 1)
d = mod_inverse(e, totient)
print("d\n" + str(d))

plaintext = pow(ciphertext, d, n)
print("plaintext\n" + str(plaintext))

# Final send isn't required
# do_the_send(r, plaintext)

print(hex(plaintext)[2:].decode("hex"))

