#!/usr/bin/python

import json
from collections import Counter
from pwn import *
import time
import re

def you_shall_receive():
	response = r.recv(1000)
	log.info(response)
	return response

def do_the_send(remote, message):
	remote.send(str(message) + "\n")
	time.sleep(3)


with open('incidents.json') as incidents_file:
	incident_data = json.load(incidents_file)
	incidents = incident_data['tickets']

	source_dest = []

	for incident in incidents:
		source_dest.append((incident['src_ip'], incident['dst_ip'], incident['file_hash']))


	r = remote('2018shell.picoctf.com', 63299)

	# Send most common source IP
	src_ip_count = Counter([tup[0] for tup in source_dest])
	do_the_send(r, src_ip_count.most_common(1)[0][0])

	response = you_shall_receive()

	# Find unique destination ips that was targetted by this source
	ip_regex = re.compile("\d+")
	match = ip_regex.findall(response)

	unique_dest_ip_from = ".".join(match) # Awful AWFUL variable naming

	# Send the answer
	the_answer = len(set([tup[1] for tup in source_dest if tup[0] == unique_dest_ip_from]))
	do_the_send(r, the_answer)

	response = you_shall_receive()


	# Find number of unique dest ips a file is sent, on average to 2 decimal places
	files = set([tup[2] for tup in source_dest])
	file_count = []
	
	for file in files:
		file_count.append(len(set([tup[1] for tup in source_dest if tup[2] == file])))

	# Send the new answer
	the_new_answer = round(float(sum(file_count))/len(files), 2)
	do_the_send(r, the_new_answer)

	you_shall_receive()
