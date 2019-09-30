#!/bin/bash

part1=`curl -s https://2019shell1.picoctf.com/problem/21519/ | grep -oE "picoCTF{[0-9a-z_]*"`
part2=`curl -s https://2019shell1.picoctf.com/problem/21519/mycss.css | grep -oE "[0-9a-z]+_[0-9a-z]+_[0-9a-z]+"`
part3=`curl -s https://2019shell1.picoctf.com/problem/21519/myjs.js | grep -oE "_[a-z]+\?[0-9a-z]+}"`

printf "%s%s%s\n" ${part1} ${part2} ${part3} | tee flag.txt
