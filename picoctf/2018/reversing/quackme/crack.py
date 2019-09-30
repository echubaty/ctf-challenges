#!/usr/bin/python

import pwn

greeting = "You have now entered the Duck Web, and you're in for a honkin' good time.\nCan you figure out my trick?"
secret_buffer = "\x29\x06\x16\x4f\x2b\x35\x30\x1e\x51\x1b\x5b\x14\x4b\x08\x5d\x2b\x53\x10\x54\x51\x43\x4d\x5c\x54\x5d\x00"

print(pwn.xor(greeting, secret_buffer))
