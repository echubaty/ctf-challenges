#!/usr/bin/python

numbers = open("thenumbers.txt", "r").read().split()

output = ""

for x in numbers:
	if x.isdigit():
		output += chr(int(x) - 1 + ord('A'))
	else:
		output += x

print(output)
