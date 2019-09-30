#!/bin/bash

curl -s -A "Googlebot-News" http://2018shell.picoctf.com:60372/flag | grep -o -E "picoCTF\{[a-zA-Z0-9_]*\}"
