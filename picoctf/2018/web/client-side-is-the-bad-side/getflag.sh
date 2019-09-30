#!/bin/bash

curl -s http://2018shell.picoctf.com:53990 | grep -o -E "== '[a-zA-Z0-9_\{\}]*'" | cut -d "'" -f 2 | tac | tr -d '\n' && echo
