#!/bin/bash

unshadow ./passwd ./shadow > pass.txt 

john --wordlist=/usr/share/wordlists/rockyou.txt ./pass.txt &>/dev/null

user=$(john -show ./pass.txt | head -n 1 | cut -d ":" -f 1)
pass=$(john -show ./pass.txt | head -n 1 | cut -d ":" -f 2)

# root:password1

echo -e "$user\n$pass" | nc 2018shell.picoctf.com 5221 | grep -oE picoCTF{.*}