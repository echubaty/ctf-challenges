#!/bin/bash

wget -q --post-file="post.out" http://2018shell.picoctf.com:7949/button2.php
grep -o -E "picoCTF{.*}" button2.php
