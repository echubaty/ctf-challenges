#!/bin/bash

printf "picoCTF{%s}\n" `echo "bDNhcm5fdGgzX3IwcDM1" | base64 -d` | tee flag.txt
