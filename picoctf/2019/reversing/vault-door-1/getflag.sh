#!/bin/bash

# This is awful (but it works)
printf "picoCTF{%s}\n" `grep -E "password.charAt\(" VaultDoor1.java | awk -F '==' '{print $1, $2}' | sort -V | cut -d " " -f 19,20 | tr -d "' &;\n" ` | tee flag.txt
