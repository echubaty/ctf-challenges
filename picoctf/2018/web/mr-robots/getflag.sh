#!/bin/bash

curl -s http://2018shell.picoctf.com:10157/143ce.html | grep -o -E "picoCTF\{[a-zA-Z0-9_]*\}"
