#!/bin/bash

printf "picoCTF{%s}\n" `grep "password.equals" VaultDoorTraining.java | cut -d "\"" -f 2` | tee flag.txt
