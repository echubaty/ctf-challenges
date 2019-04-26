#!/bin/bash

part1=`curl -s 2018shell.picoctf.com:47428 | grep -E -o "picoCTF\{[0-9a-zA-Z_]*"`
part2=`curl -s http://2018shell.picoctf.com:47428/mycss.css | grep -E -o "[0-9a-zA-Z_]+\}"`

printf "%s%s\n" ${part1} ${part2}