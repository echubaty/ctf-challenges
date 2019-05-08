#!/usr/bin/python

from pwn import *

def you_shall_receive():
	response = r.recv(1000)
	log.info(response)
	return response

def do_the_send(remote, message):
	remote.send(str(message) + "\n")
	time.sleep(3)

r = remote('2018shell.picoctf.com', 50875)

time_estimates = {'00:00:00': 11000,
'00:15:00' : 11000,
'00:30:00' : 11000,
'00:45:00' : 11000,
'01:00:00' : 11000,
'01:15:00' : 11000,
'01:30:00' : 11000,
'01:45:00' : 11000,
'02:00:00' : 11000,
'02:15:00' : 11000,
'02:30:00' : 11000,
'02:45:00' : 11000,
'03:00:00' : 11000,
'03:15:00' : 11000,
'03:30:00' : 11000,
'03:45:00' : 11000,
'04:00:00' : 11000,
'04:15:00' : 11000,
'04:30:00' : 11000,
'04:45:00' : 11000,
'05:00:00' : 11000,
'05:15:00' : 11000,
'05:30:00' : 11000,
'05:45:00' : 11000,
'06:00:00' : 11000,
'06:15:00' : 11000,
'06:30:00' : 11000,
'06:45:00' : 11000,
'07:00:00' : 11000,
'07:15:00' : 11000,
'07:30:00' : 11000,
'07:45:00' : 14000,
'08:00:00' : 14000,
'08:15:00' : 13000,
'08:30:00' : 12000,
'08:45:00' : 12000,
'09:00:00' : 11000,
'09:15:00' : 11000,
'09:30:00' : 11000,
'09:45:00' : 11000,
'10:00:00' : 11000,
'10:15:00' : 11000,
'10:30:00' : 11000,
'10:45:00' : 11000,
'11:00:00' : 12000,
'11:15:00' : 13000,
'11:30:00' : 14000,
'11:45:00' : 17000,
'12:00:00' : 18000,
'12:15:00' : 15000,
'12:30:00' : 15000,
'12:45:00' : 13000,
'13:00:00' : 12000,
'13:15:00' : 11000,
'13:30:00' : 11000,
'13:45:00' : 11000,
'14:00:00' : 11000,
'14:15:00' : 11000,
'14:30:00' : 11000,
'14:45:00' : 11000,
'15:00:00' : 11000,
'15:15:00' : 11000,
'15:30:00' : 11000,
'15:45:00' : 11000,
'16:00:00' : 11000,
'16:15:00' : 11000,
'16:30:00' : 11000,
'16:45:00' : 11000,
'17:00:00' : 11000,
'17:15:00' : 12000,
'17:30:00' : 13000,
'17:45:00' : 14000,
'18:00:00' : 14500,
'18:15:00' : 17000,
'18:30:00' : 15000,
'18:45:00' : 15000,
'19:00:00' : 14000,
'19:15:00' : 14000,
'19:30:00' : 13000,
'19:45:00' : 12000,
'20:00:00' : 11000,
'20:15:00' : 11000,
'20:30:00' : 11000,
'20:45:00' : 11000,
'21:00:00' : 11000,
'21:15:00' : 11000,
'21:30:00' : 11000,
'21:45:00' : 11000,
'22:00:00' : 11000,
'22:15:00' : 11000,
'22:30:00' : 11000,
'22:45:00' : 11000,
'23:00:00' : 11000,
'23:15:00' : 11000,
'23:30:00' : 11000,
'23:45:00' : 11000}

response = you_shall_receive().split('\n')[-15:-1]

outliers = [x.split()[0] for x in response if len(x) > 2 and time_estimates[x.split()[2]] < int(x.split()[3])]

log.info(' '.join(outliers))

do_the_send(r, ' '.join(outliers))
you_shall_receive()
